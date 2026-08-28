"""Clean the restaurant narrative corpus JSON.

Reads ``restaurant_corpus_initial.json`` (the Inclezan et al. restaurant
narrative corpus) and writes ``restaurant_corpus_clean.json``, dropping the
``source`` field and replacing ``logic_form`` with ``"N/A"`` for each record.
"""
import json
import os

def clean_json(input_json, output_json):
    # Load the original JSON data
    with open(input_json, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Process each story
    for story in data:
        # Remove 'source' key if it exists
        if 'source' in story:
            del story['source']
        
        # Replace 'logic_form' with "N/A"
        story['logic_form'] = "N/A"
    
    # Save the cleaned data
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Cleaned JSON saved to: {output_json}")

if __name__ == "__main__":
    # Adjust paths based on your structure:
    # Script is in RESEARCH/data/code/
    # JSON is in RESEARCH/data/restaurant_data/
    input_file = '../restaurant_data/restaurant_corpus_initial.json'
    output_file = '../restaurant_data/restaurant_corpus_clean.json'
    
    # Safety check
    if not os.path.exists(input_file):
        print(f"❌ Input file not found: {os.path.abspath(input_file)}")
        exit(1)
    
    clean_json(input_file, output_file)