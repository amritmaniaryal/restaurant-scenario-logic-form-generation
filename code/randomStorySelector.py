import json
import random
import os # Import the os module

# Get the directory where the script is located
script_dir = os.path.dirname(__file__) 

# === CONFIGURATION ===
# Build the path relative to the script's directory
input_file = os.path.join(script_dir, '../experiments/StoryGeneration/generated_stories_gemini.json')
output_file = os.path.join(script_dir, '../encodedForm/random_30_entries_1.json')
num_entries = 30
# =====================

def select_random_entries(data_json, num_entries=30):
    if "data" not in data_json:
        raise KeyError("Input JSON must contain a 'data' key.")
    entries = data_json["data"]
    if len(entries) < num_entries:
        raise ValueError(f"Requested {num_entries} entries, but only {len(entries)} available.")
    random_entries = random.sample(entries, num_entries)
    return {
        "metadata": data_json.get("metadata", {}),
        "data": random_entries
    }

def main():
    # Load input JSON
    with open(input_file, 'r', encoding='utf-8') as f:
        full_data = json.load(f)

    # Sample entries
    sampled_data = select_random_entries(full_data, num_entries=num_entries)

    # Save output
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(sampled_data, f, indent=2)

    print(f"Saved {num_entries} random entries to '{output_file}'")

if __name__ == "__main__":
    main()