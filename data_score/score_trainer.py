import json
import random
from datetime import datetime

import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
from torch.utils.data import DataLoader, TensorDataset
from tqdm import tqdm
import matplotlib.pyplot as plt
from tensorboardX import SummaryWriter


# writer = SummaryWriter()


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


def evaluate():
    model.eval()
    correct = 0
    wrong = 0
    total = 0
    with torch.no_grad():
        for metric_, score_ in val_loader:
            outputs = model(metric_)
            boolean_scores = (score_ > 0.2).to(torch.int)
            length = torch.sum(boolean_scores, dim=1)
            for i in range(len(outputs)):
                # _, idx = torch.max(outputs[i], dim=0)
                # if boolean_scores[i][idx.item()] == 1:
                if all(torch.topk(outputs[i], k=length[i])[0] ==
                       torch.topk(outputs[i] * boolean_scores[i], k=length[i])[0]):
                    correct += 1
                else:
                    wrong += 1
            total += score_.size()[0]
    assert correct + wrong == total
    accuracy = correct / total
    print(f'Validation Accuracy: {accuracy * 100:.2f}%')
    if accuracy > 0.55:
        current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        torch.save(model.state_dict(), f'models/{current_datetime}__{accuracy}__batch{batch_size}.pth')
    return accuracy


input_size = 8
num_classes = 5

hidden_size = 16
batch_size = 4
print(batch_size)
num_epochs = 160
lr = 5e-4
data_version = 7

# writer.add_hparams({
#     "hidden size": hidden_size,
#     "batch size": batch_size,
#     "epochs": num_epochs,
#     "lr": lr,
#     "data version": data_version
# }, {})
with open(f'score_data_{data_version}.json') as f:
    data = json.load(f)

metrics = []
scores = []
for item in data:
    metrics.append(list(item["metrics"].values()))
    scores.append(item["scores"])
metrics = torch.tensor(metrics, dtype=torch.float)
scores = torch.tensor(scores, dtype=torch.float)

metric_train, metric_val, score_train, score_val = train_test_split(metrics, scores, test_size=0.2, random_state=42)

train_dataset = TensorDataset(metric_train, score_train)
val_dataset = TensorDataset(metric_val, score_val)

train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)
val_loader = DataLoader(dataset=val_dataset, batch_size=batch_size, shuffle=False)

model = ClassifierModel(input_size, hidden_size, num_classes)
optimizer = optim.Adam(model.parameters(), lr=lr)


for epoch in range(num_epochs):
    model.train()
    running_loss = 0.0
    for metric, score in train_loader:
        optimizer.zero_grad()
        output = model(metric)
        loss = torch.norm(output - score, dim=1).sum()
        loss.backward()
        optimizer.step()
        running_loss += loss.item()
    epoch_loss = running_loss / len(data)
    print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {epoch_loss:.4f}')
    evaluate()
    # writer.add_scalar('Train/Loss', epoch_loss, epoch)
    # writer.add_scalar('Validation/Accuracy', evaluate(), epoch)
