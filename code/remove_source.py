import json
import os

# Get the directory where the script is located
script_dir = os.path.dirname(__file__) 

# === CONFIGURATION ===
# Build the path relative to the script's directory
input_file = os.path.join(script_dir, '../restaurant_data/restaurant_corpus_initial.json')
output_file = os.path.join(script_dir, '../restaurant_data/restaurant_corpus_no_source.json')

# Read the JSON data
with open(input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Remove the 'source' key from each dictionary in the list
for item in data:
    item.pop('source', None)  # Use pop with default to avoid KeyError if 'source' is missing

# Write the cleaned data back to a new JSON file
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Successfully removed 'source' field and saved to {output_file}")