import json
import os

def rename_and_reorder(input_json, output_json):
    # Load the original JSON
    with open(input_json, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Define the new key mapping and order
    key_mapping = {
        "Scenario Number": "sid",
        "Story": "text",
        "Logic Form": "logic_form",
        "Type": "scenario_type"
    }

    # Desired order of keys in output
    key_order = ["sid", "text", "logic_form", "scenario_type"]
    
    cleaned_data = []
    
    for item in data:
        new_item = {}
        
        # Map old keys to new keys
        for old_key, new_key in key_mapping.items():
            if old_key in item:
                value = item[old_key]
                # Convert sid to integer if possible
                if new_key == "sid":
                    try:
                        value = int(value)
                    except (ValueError, TypeError):
                        pass  # Keep as-is if not convertible
                new_item[new_key] = value
            else:
                # Optional: handle missing keys
                new_item[new_key] = None  # or skip, depending on your need
        
        # Reorder keys explicitly
        ordered_item = {key: new_item[key] for key in key_order if key in new_item}
        cleaned_data.append(ordered_item)
    
    # Save to new file
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(cleaned_data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Renamed and reordered JSON saved to: {output_json}")

if __name__ == "__main__":
    # Adjust paths as needed
    input_file = "../restaurant_data/restaurant_scenarios_clean_100.json"       
    output_file = "../restaurant_data/restaurant_scenarios_clean_100_2.json" 
    
    if not os.path.exists(input_file):
        print(f"❌ Input file not found: {os.path.abspath(input_file)}")
        exit(1)
    
    rename_and_reorder(input_file, output_file)