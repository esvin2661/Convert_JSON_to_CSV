
import csv
import json

def json_to_csv(json_data, csv_file):
    # Assuming the JSON data is a list of dictionaries
    data_list = json.loads(json_data)

    # Extract column headers from the first dictionary
    headers = data_list[0].keys()

    with open(csv_file, 'w', newline='') as csv_file:
        # Create a CSV writer
        csv_writer = csv.DictWriter(csv_file, fieldnames=headers)

        # Write header row
        csv_writer.writeheader()

        # Write data rows
        csv_writer.writerows(data_list)

if __name__ == "__main__":
    # Example JSON data
    example_json = '[{"Name": "John", "Age": 25, "City": "New York"}, {"Name": "Alice", "Age": 22, "City": "San Francisco"}]'

    # Specify the desired CSV file name
    output_csv_file = 'output.csv'

    # Convert JSON to CSV
    json_to_csv(example_json, output_csv_file)
    print(f"Conversion completed. CSV file saved as {output_csv_file}")
