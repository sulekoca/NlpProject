import csv
import json

# Set a new, large field size limit
max_int_c_long = 2147483647  # This is the max size for a C long on many systems
csv.field_size_limit(max_int_c_long)

# Function to read CSV file and convert to Alpaca-style instruction format
def convert_csv_to_alpaca(csv_file):
    alpaca_style_datasets = []
    with open(csv_file, "r", encoding="utf-8") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            content = row['content'].replace('""', '"')
            abstract = row['abstract'].replace('""', '"')
            alpaca_instance = {
                "instruction": "Aşağıdaki metni özetle",
                "input": content,
                "output": abstract
            }
            alpaca_style_datasets.append(alpaca_instance)
    return alpaca_style_datasets

# Convert each CSV file to Alpaca-style instruction format
csv_files = ["TR_news_train.csv"]  # Add your CSV file names here
combined_dataset = []
for csv_file in csv_files:
    alpaca_datasets = convert_csv_to_alpaca(csv_file)
    combined_dataset.extend(alpaca_datasets)

# Save combined dataset as a single JSON file
with open("CSE4078S24_Grp8_AlpacaStyle_TR_news.json", "w", encoding="utf-8") as f:
    json.dump(combined_dataset, f, ensure_ascii=False, indent=4)

print("All datasets converted and saved successfully.")
