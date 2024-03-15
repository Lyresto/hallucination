import json

import torch
import torch.nn as nn
from torch import argmax
from tqdm import tqdm


class ClassifierModel(nn.Module):
    def __init__(self, input_size_, hidden_size_, num_classes_):
        super(ClassifierModel, self).__init__()
        self.fc1 = nn.Linear(input_size_, hidden_size_)
        self.sig = nn.Sigmoid()
        self.fc2 = nn.Linear(hidden_size_, num_classes_)

    def forward(self, x):
        x = self.fc1(x)
        x = self.sig(x)
        x = self.fc2(x)
        return x


model = ClassifierModel(7, 16, 5)
model.load_state_dict(torch.load('models/2023-12-01_22-35-03__0.5730337078651685__batch2.pth'))
model.eval()

with open('../code_alpaca_20k_filtered_6.json') as f:
    data = json.load(f)

type_cnt = [0] * 5
for item in tqdm(data):
    metrics = list(item["metrics"].values())[:7]
    scores = model(torch.tensor(metrics).to(torch.float))
    if item == data[0]:
        print(scores)
    item["scores"] = scores.tolist()
    type_cnt[argmax(scores).item()] += 1

print(type_cnt)
print([it / sum(type_cnt) for it in type_cnt])
# with open('../code_alpaca_20k_filtered_6.json', 'w+') as f:
#     f.write(json.dumps(data, indent=4))
