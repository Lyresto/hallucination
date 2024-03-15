import json
from tqdm import tqdm

with open('code_alpaca_20k_filtered_7.json') as f:
    data = json.load(f)

cnt = 0
for item in tqdm(data):
    prompt = item["instruction"]
    code = item["output"]
    ipt = item["input"]
    metrics = item["metrics"]
    exclusion = [0] * 5
    recommend = [0] * 5
    if metrics["prompt length"] >= 70:
        exclusion[0] = 1

    if metrics["code lines"] <= 3:
        recommend[1] = 1
        cnt += 1
    # if metrics["code lines"] < 8 and metrics["code complexity"] < 20:
    #     exclusion[1] = 1

    if len(ipt) == 0:
        exclusion[2] = 1
    if metrics["code lines"] >= 8:
        recommend[2] = 1
    if metrics["similarity between prompt and code"] >= 50:
        recommend[2] = 1

    if metrics["code lines"] >= 8:
        recommend[3] = 1
    if "import " in code:
        recommend[3] = 5

    if metrics["code lines"] >= 4:
        recommend[4] = 1
    item["recommend"] = recommend
    item["exclusion"] = exclusion

print(cnt)
with open('code_alpaca_20k_filtered_7.json', 'w+') as f:
    f.write(json.dumps(data, indent=4))

