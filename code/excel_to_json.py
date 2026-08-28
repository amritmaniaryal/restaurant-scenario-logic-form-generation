import json
import os
import pandas as pd  # Requires: pip install pandas openpyxl

# --- Configuration ---
excel_file = './restaurant_scenarios.xlsx'  # Update with your actual filename
output_json = './restaurant_data/scenarios_and_logic_form.json'

# Create output folder if it doesn't exist
os.makedirs('./restaurant_data', exist_ok=True)

# Check if the Excel file exists
if not os.path.exists(excel_file):
    print(f"❌ Error: Excel file not found at {os.path.abspath(excel_file)}")
else:
    print(f"✅ Loading Excel file: {excel_file}")

    try:
        # Read the Excel file
        df = pd.read_excel(excel_file)

        # Optional: Print columns to verify names (in case of typos)
        print("📊 Columns in Excel:", list(df.columns))

        # Clean up column names (remove extra spaces, etc.)
        df.columns = df.columns.str.strip()

        # Required columns
        required_cols = ["Scenario Number", "Type", "Story", "Logic Form"]
        missing_cols = [col for col in required_cols if col not in df.columns]

        if missing_cols:
            print(f"❌ Missing required columns in Excel: {missing_cols}")
        else:
            # Convert to list of dictionaries
            scenarios = df[required_cols].to_dict(orient='records')

            # Save as pretty-printed JSON
            with open(output_json, 'w', encoding='utf-8') as f:
                json.dump(scenarios, f, indent=4, ensure_ascii=False)

            print(f"✅ Successfully converted {len(scenarios)} rows from Excel to JSON.")
            print(f"📄 Saved to: {os.path.abspath(output_json)}")

    except Exception as e:
        print(f"❌ Error processing Excel file: {e}")