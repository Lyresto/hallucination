import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import torch
import numpy as np
a = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import torch
import numpy as np
a = torch.ones(5)
a_np = np.ones(5)

#print(a_np)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(a_np, file)
