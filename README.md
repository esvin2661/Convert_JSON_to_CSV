# JSON to CSV Converter

This Python script converts JSON data to CSV format using the `json` and `csv` modules.

## Usage

1. Replace the `example_json` variable in the script (`json_to_csv.py`) with your actual JSON data.
2. Specify the desired CSV file name in the `output_csv_file` variable.
3. Run the script:

```bash
python json_to_csv.py

Example:

# Example JSON data
example_json = '[{"Name": "John", "Age": 25, "City": "New York"}, {"Name": "Alice", "Age": 22, "City": "San Francisco"}]'

# Specify the desired CSV file name
output_csv_file = 'output.csv'

# Convert JSON to CSV
json_to_csv(example_json, output_csv_file)
print(f"Conversion completed. CSV file saved as {output_csv_file}")



