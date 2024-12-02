import json
import os

folder_path = 'CSE4078S24_GRP8/delivery2/datasets'

json_files = [file for file in os.listdir(folder_path) if file.endswith('.json')]

combined_data = []

# Iterating through each JSON file
for file_name in json_files:
    file_path = os.path.join(folder_path, file_name)

    # Opening and loading data from each JSON file with explicit encoding
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        combined_data.extend(data)

output_file_path = 'CSE4078S24_GRP8/delivery2/datasets/CSE4078S24_Grp8_AlpacaStyle_Combined_Dataset.json'

# Writing the combined data to the output JSON file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    json.dump(combined_data, output_file, indent=4, ensure_ascii=False)

print(f"Combined dataset saved to: {output_file_path}")
