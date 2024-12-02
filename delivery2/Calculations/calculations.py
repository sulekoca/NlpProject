import json
import statistics

# Type the dataset name
with open('dataset.json', encoding='utf-8') as f:
    data = json.load(f)

# Initializing variables
num_instructions = len(data)
input_lengths = [len(item['input']) for item in data]
output_lengths = [len(item['output']) for item in data]

# Calculating standart deviation, avg. input and output lengths and number of instructions
avg_instructions = num_instructions
avg_input_length = statistics.mean(input_lengths)
avg_output_length = statistics.mean(output_lengths)
std_dev = statistics.stdev(input_lengths + output_lengths)

# Printing the statistics
print(f"Number of instructions: {num_instructions}")
print(f"Average of instructions: {avg_instructions}")
print(f"Average input length: {avg_input_length}")
print(f"Average output length: {avg_output_length}")
print(f"Standard deviation: {std_dev}")
