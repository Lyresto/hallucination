import json

with open('../inject/code_alpaca_20k_filtered_7.json') as f:
    data = json.load(f)

with open('../generate_results/generate1_filter3.json') as f:
    gene = json.load(f)

merged_data = []
for i, item in enumerate(data):
    gene_code = gene[str(i)]["hall code"]
    merge_item = {"instruction": item["instruction"], "input": item["input"], "output": item["output"],
                  "hall_code": gene_code, "hall_type": item["distributed type"]}
    merged_data.append(merge_item)

with open('result.json', 'w+') as f:
    f.write(json.dumps(merged_data, indent=4))
