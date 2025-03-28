import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import numpy as np
import pandas as pd
import torch

MyNet = torch.nn.Sequential(torch.nn.Linear(4, 15),
                            torch.nn.Sigmoid(),
                            torch.nn.Linear(15, 3),
                            )
MyNet.load_state_dict(torch.load("my_model.pt"))
input = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
### BEGIN SOLUTION
from collections import Counter



def predict_allCharacters(input):
    output = MyNet(input)
    return [i[1] for i in Counter(output.reshape(1, 3)).most_common(1)]



### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(confidence_score, f)
