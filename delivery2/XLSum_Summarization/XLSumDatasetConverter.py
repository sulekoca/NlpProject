import json

# Fix JSON format
def fix_json_format(json_file):
    with open(json_file, "r", encoding="utf-8") as file:
        data = file.readlines()
    data[0] = '[' + data[0]
    data[-1] = data[-1].rstrip() + ']'
    data = ','.join(data)
    with open(json_file, "w", encoding="utf-8") as file:
        file.write(data)

# Convert to alpaca
def convert_json_to_alpaca(json_file):
    with open(json_file, "r", encoding="utf-8") as file:
        data = json.load(file)
    alpaca_style_datasets = []
    for item in data:
        alpaca_instance = {
            "instruction": "Aşağıdaki metni özetle",
            "input": item["text"],
            "output": item["summary"]
        }
        alpaca_style_datasets.append(alpaca_instance)
    return alpaca_style_datasets

json_file = "turkish_train.jsonl"
fix_json_format(json_file)

alpaca_datasets = convert_json_to_alpaca(json_file)

output_file = "alpaca_dataset_turkish_train.json"
with open(output_file, "w", encoding="utf-8") as file:
    json.dump(alpaca_datasets, file, ensure_ascii=False, indent=4)
