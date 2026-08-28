"""Load and filter the ROCStories corpus for restaurant-related stories.

Reads the official ROCStories CSV, keeps only stories whose titles match
restaurant keywords, and writes the filtered subset to JSON together with a
filtering log.

NOTE: The raw ROCStories corpus is not redistributed in this repository; see
RECONSTRUCTION.md for how to obtain it.
"""
import pandas as pd
import os
import json
import re
from typing import List, Set, Optional, Dict, Any
from datetime import datetime
from pathlib import Path
import sys

def get_restaurant_keywords() -> Set[str]:
    """
    Returns a set of keywords commonly associated with restaurant visits.
    
    Returns:
        Set[str]: Keywords related to restaurants and dining experiences
    """
    restaurant_keywords = {
        # Core restaurant terms
        'restaurant', 'steakhouse', 'pizzeria', 'diner', 'order', 'sushi', 
        # 'diner', 'cafe', 'café', 'bistro', 'eatery', 'brasserie',
        # 'steakhouse', 'pizzeria', 'sushi', 'bar', 'pub', 'tavern', 'grill',
        # 'buffet', 'dinner', 'lunch',
        # 'takeout', 'take-out', 'menu', 'waiter', 'waitress', 'server', 'chef', 
        # 'cook', 'reservation', 'booking', 'drive-thru',
        # 'fine dining', 'casual dining', 'dining',
        # 'dined', 'ordered', 'order', 'bill', 'check', 'tip', 'gratuity',
        # 'bartender', 'appetizer', 'entree', 'entrée', 'course',
        # 'salad', 'soup', 'sandwich', 'burger', 'pizza', 'pasta', 'steak',
        # 'chicken', 'fish', 'seafood', 'vegetarian', 'vegan', 'gluten',
        # 'delicious', 'tasty', 'yummy','overcooked', 'undercooked',
        # 'burnt', 'salty', 'sweet', 'sour', 'bitter', 'umami', 'flavor', 'taste',
        # 'hungry', 'starving', 'full', 'satisfied', 'unsatisfied', 'compliment', 'review', 'yelp',
        # 'google review', 'tripadvisor', 'reservation',
        # 'ambiance', 'live music', 'anniversary', 'date','party','local', 'family-owned',
        # 'buffet', 'all-you-can-eat', 'tasting menu', 'daily special', 'happy hour'
    }
    return restaurant_keywords

def preprocess_text(text: str) -> str:
    """
    Preprocesses text by converting to lowercase and removing extra whitespace.
    
    Args:
        text (str): Input text to preprocess
        
    Returns:
        str: Preprocessed text
    """
    if pd.isna(text):
        return ""
    return re.sub(r'\s+', ' ', str(text).lower().strip())

def contains_restaurant_keywords(text: str, keywords: Set[str]) -> bool:
    """
    Checks if the given text contains any restaurant-related keywords.
    
    Args:
        text (str): Text to check
        keywords (Set[str]): Set of keywords to search for
        
    Returns:
        bool: True if any keyword is found, False otherwise
    """
    if not text:
        return False
    
    # Create a regex pattern that matches whole words only
    pattern = r'\b(?:' + '|'.join(re.escape(word) for word in keywords) + r')\b'
    return bool(re.search(pattern, text, re.IGNORECASE))

def filter_restaurant_stories(df: pd.DataFrame, 
                            title_column: str = 'storytitle',
                            keywords: Optional[Set[str]] = None) -> pd.DataFrame:
    """
    Filters DataFrame to return only rows with restaurant-related story titles.
    
    Args:
        df (pd.DataFrame): Input DataFrame
        title_column (str): Column name containing story titles
        keywords (Optional[Set[str]]): Custom keywords to use. If None, uses default.
        
    Returns:
        pd.DataFrame: Filtered DataFrame containing only restaurant-related stories
    """
    if keywords is None:
        keywords = get_restaurant_keywords()
    
    # Preprocess titles
    processed_titles = df[title_column].apply(preprocess_text)
    
    # Filter rows that contain restaurant keywords
    mask = processed_titles.apply(lambda x: contains_restaurant_keywords(x, keywords))
    
    return df[mask].copy()

def combine_sentences_to_story(row: pd.Series, sentence_columns: List[str] = None) -> str:
    """
    Combines sentence columns into a single story string.
    
    Args:
        row (pd.Series): DataFrame row
        sentence_columns (List[str]): List of sentence column names
        
    Returns:
        str: Combined story text
    """
    if sentence_columns is None:
        sentence_columns = [f'sentence{i}' for i in range(1, 6)]
    
    sentences = []
    for col in sentence_columns:
        if col in row and pd.notna(row[col]):
            sentences.append(str(row[col]).strip())
    
    return ' '.join(sentences)

def create_json_structure(df: pd.DataFrame, 
                         original_total: int,
                         sentence_columns: List[str] = None) -> Dict[str, Any]:
    """
    Creates the JSON structure with metadata and story data.
    
    Args:
        df (pd.DataFrame): Filtered DataFrame
        original_total (int): Total number of stories in original dataset
        sentence_columns (List[str]): Sentence column names
        
    Returns:
        Dict[str, Any]: JSON structure with metadata and stories
    """
    if sentence_columns is None:
        sentence_columns = [f'sentence{i}' for i in range(1, 6)]
    
    # Create stories list
    stories = []
    for _, row in df.iterrows():
        story_dict = {
            'storyid': row['storyid'] if 'storyid' in row else None,
            'storytitle': row['storytitle'] if 'storytitle' in row else '',
            'story': combine_sentences_to_story(row, sentence_columns)
        }
        stories.append(story_dict)
    
    # Create metadata
    metadata = {
        'extraction_timestamp': datetime.now().isoformat(),
        'filter_criteria': 'restaurant-related stories',
        'original_total_stories': original_total,
        'filtered_stories_count': len(stories),
        'filter_percentage': round((len(stories) / original_total) * 100, 2) if original_total > 0 else 0,
        'sentence_columns_used': sentence_columns,
        'keywords_used_count': len(get_restaurant_keywords())
    }
    
    return {
        'metadata': metadata,
        'stories': stories
    }

def load_csv_data(filepath: str) -> pd.DataFrame:
    """
    Loads CSV data into a pandas DataFrame.
    
    Args:
        filepath (str): Path to the CSV file
        
    Returns:
        pd.DataFrame: Loaded DataFrame
    """
    try:
        df = pd.read_csv(filepath)
        print(f"Successfully loaded {len(df)} rows from {filepath}")
        return df
    except FileNotFoundError:
        print(f"Error: File {filepath} not found.")
        raise
    except Exception as e:
        print(f"Error loading CSV: {e}")
        raise

def save_json_data(data: Dict[str, Any], output_filepath: str) -> None:
    """
    Saves data to a JSON file with proper formatting.
    
    Args:
        data (Dict[str, Any]): Data to save
        output_filepath (str): Output file path
    """
    try:
        # Ensure the directory exists
        Path(output_filepath).parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Saved JSON data to {output_filepath}")
    except Exception as e:
        print(f"Error saving JSON: {e}")
        raise

def create_log_entry(keywords: Set[str], 
                    original_total: int, 
                    filtered_count: int,
                    input_file: str,
                    output_file: str) -> Dict[str, Any]:
    """
    Creates a log entry with statistics and keywords used.
    
    Args:
        keywords (Set[str]): Keywords used for filtering
        original_total (int): Total stories in original dataset
        filtered_count (int): Number of filtered stories
        input_file (str): Input file path
        output_file (str): Output file path
        
    Returns:
        Dict[str, Any]: Log entry dictionary
    """
    filter_percentage = round((filtered_count / original_total) * 100, 2) if original_total > 0 else 0
    
    return {
        "timestamp": datetime.now().isoformat(),
        "input_file": str(input_file),
        "output_file": str(output_file),
        "original_total_stories": original_total,
        "filtered_stories_count": filtered_count,
        "filter_percentage": filter_percentage,
        "keywords_used_count": len(keywords),
        "keywords": sorted(list(keywords))  # Sort for consistent ordering
    }

def save_or_append_log(log_entry: Dict[str, Any], log_file_path: Path) -> None:
    """
    Saves log entry to a JSON file, appending to existing entries if file exists.
    """
    try:
        # Ensure the directory exists
        log_file_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Check if log file exists and read existing entries
        existing_entries = []
        if log_file_path.exists():
            try:
                with open(log_file_path, 'r', encoding='utf-8') as f:
                    content = f.read().strip()
                    if content:  # Only parse if there's content
                        existing_entries = json.loads(content)
                        if not isinstance(existing_entries, list):
                            print(f"Warning: Log file format unexpected, starting fresh")
                            existing_entries = []
                    # If content is empty, keep existing_entries as empty list
            except json.JSONDecodeError:
                print(f"Warning: Could not parse existing log file, starting fresh")
                existing_entries = []
        else:
            print(f"Creating new log file at {log_file_path}")
        
        # Append new entry
        existing_entries.append(log_entry)
        
        # Save updated log data
        with open(log_file_path, 'w', encoding='utf-8') as f:
            json.dump(existing_entries, f, indent=2, ensure_ascii=False)
        
        print(f"✓ Log entry saved successfully to {log_file_path}")
        print(f"Total log entries now: {len(existing_entries)}")
        
    except Exception as e:
        print(f"❌ Error saving log entry: {e}")
        import traceback
        traceback.print_exc()

def test_log_creation():
    """Test function to debug log creation"""
    base_dir = Path(__file__).resolve().parent
    log_file = base_dir.parent / "other_data" / "filtering_log.json"
    
    print(f"Testing log creation...")
    print(f"Log file path: {log_file}")
    print(f"Directory exists: {log_file.parent.exists()}")
    print(f"Directory writable: {os.access(log_file.parent, os.W_OK)}")
    
    # Test creating a simple log entry
    test_entry = {
        "timestamp": datetime.now().isoformat(),
        "test": "This is a test entry"
    }
    
    try:
        save_or_append_log(test_entry, log_file)
        print("Test log creation: SUCCESS")
    except Exception as e:
        print(f"Test log creation: FAILED - {e}")
        import traceback
        traceback.print_exc()

def main():
    """
    Main function to demonstrate the filtering process and output JSON.
    """
    # Configuration - resolve paths relative to this script file
    base_dir = Path(__file__).resolve().parent
    input_file = base_dir.parent / "other_data" / "ROCStories.csv"
    output_file = base_dir.parent / "other_data" / "roc_to_json.json"
    log_file = base_dir.parent / "other_data" / "filtering_log.json"
    
    print(f"Input file path: {input_file}")
    print(f"Output file path: {output_file}")
    print(f"Log file path: {log_file}")
    
    try:
        # Load data
        df = load_csv_data(str(input_file))

        # Store original count for metadata
        original_total = len(df)

        # Get keywords for logging
        keywords = get_restaurant_keywords()
        print(f"Using {len(keywords)} keywords for filtering")

        # Filter restaurant stories
        restaurant_df = filter_restaurant_stories(df, keywords=keywords)

        filtered_count = len(restaurant_df)
        print(f"Found {filtered_count} restaurant-related stories out of {original_total} total stories")

        # Create JSON structure
        json_data = create_json_structure(restaurant_df, original_total)

        # Save results
        save_json_data(json_data, str(output_file))

        # Create and save log entry - add explicit debugging
        print("\n--- Creating log entry ---")
        log_entry = create_log_entry(
            keywords=keywords,
            original_total=original_total,
            filtered_count=filtered_count,
            input_file=input_file,
            output_file=output_file
        )
        print(f"Log entry created: {list(log_entry.keys())}")
        print("About to save log entry...")
        
        save_or_append_log(log_entry, log_file)
        
        print("Log saving process completed.")

    except Exception as e:
        print(f"An error occurred: {e}")
        import traceback
        traceback.print_exc()

# Additional utility functions for future extensions

def add_custom_keywords(existing_keywords: Set[str], custom_keywords: List[str]) -> Set[str]:
    """
    Adds custom keywords to the existing set of restaurant keywords.
    
    Args:
        existing_keywords (Set[str]): Existing keywords
        custom_keywords (List[str]): Custom keywords to add
        
    Returns:
        Set[str]: Combined set of keywords
    """
    return existing_keywords.union(set(word.lower() for word in custom_keywords))

def filter_by_sentences(df: pd.DataFrame, sentence_columns: List[str] = None) -> pd.DataFrame:
    """
    Alternative filter that checks restaurant keywords in story sentences instead of titles.
    
    Args:
        df (pd.DataFrame): Input DataFrame
        sentence_columns (List[str]): List of sentence column names to check
        
    Returns:
        pd.DataFrame: Filtered DataFrame
    """
    if sentence_columns is None:
        sentence_columns = [f'sentence{i}' for i in range(1, 6)]
    
    keywords = get_restaurant_keywords()
    
    # Combine all sentence columns into one text per row
    combined_sentences = df[sentence_columns].apply(
        lambda row: ' '.join(str(val) for val in row if pd.notna(val)), axis=1
    )
    
    processed_sentences = combined_sentences.apply(preprocess_text)
    mask = processed_sentences.apply(lambda x: contains_restaurant_keywords(x, keywords))
    
    return df[mask].copy()

def get_statistics(df: pd.DataFrame, filtered_df: pd.DataFrame) -> dict:
    """
    Returns basic statistics about the filtering process.
    
    Args:
        df (pd.DataFrame): Original DataFrame
        filtered_df (pd.DataFrame): Filtered DataFrame
        
    Returns:
        dict: Statistics dictionary
    """
    return {
        'total_stories': len(df),
        'restaurant_stories': len(filtered_df),
        'percentage': round((len(filtered_df) / len(df)) * 100, 2) if len(df) > 0 else 0,
        'columns': list(df.columns)
    }

if __name__ == "__main__":
    main()