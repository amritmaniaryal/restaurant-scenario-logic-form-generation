import json
import os

def combine_json_files(file1_path, file2_path, output_path):
    # Load File 1: it's a direct list
    with open(file1_path, 'r', encoding='utf-8') as f:
        data1 = json.load(f)  # This should be a list
    
    # Load File 2: it's an object with a "data" key
    with open(file2_path, 'r', encoding='utf-8') as f:
        file2_content = json.load(f)
        data2 = file2_content.get("data", [])  # Extract the "data" array
    
    # Combine: append data2 to data1
    combined_data = data1 + data2
    
    # Optional: Reassign sid to be unique and sequential (if needed)
    # Uncomment the block below if you want new sequential sids
    """
    for idx, story in enumerate(combined_data, start=1):
        story["sid"] = idx
    """
    
    # Save combined data
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(combined_data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Combined {len(data1)} + {len(data2)} = {len(combined_data)} stories")
    print(f"✅ Saved to: {output_path}")

if __name__ == "__main__":
    # Adjust these paths based on your structure
    file1 = "../restaurant_data/restaurant_corpus_clean.json"      # direct array
    file2 = "../experiments/StoryGeneration/generated_stories_gemini.json"             # has {"data": [...], "metadata": ...}
    output = "../restaurant_data/combined_corpus.json"
    
    # Safety checks
    for name, path in [("File 1", file1), ("File 2", file2)]:
        if not os.path.exists(path):
            print(f"❌ {name} not found: {os.path.abspath(path)}")
            exit(1)
    
    combine_json_files(file1, file2, output)