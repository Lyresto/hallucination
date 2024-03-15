import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import numpy as np
import pandas as pd
import torch

idx, B = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
### BEGIN SOLUTION
import numpy as np
import torch
idx, B = load_data()

C =... # put solution in this variable




def index_select(ind, col_slice):
    out = []
    for i in col_slice:
        if i in ind:
            out.append(ind[i])
        else:
            out.append(np.array([]))
    return torch.LongTensor(out)



### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(C, f)
