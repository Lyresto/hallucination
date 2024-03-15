import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import numpy as np
import pandas as pd
import torch

softmax_output = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
### BEGIN SOLUTION



def load_data():
    data = np.array([[i, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
                    [0.7, 0.2, 0.1, 0.2, 0.6, 0.2, 0.1],
                    [0.2, 0.6, 0.2, 0.1, 0.1, 0.8, 0.1],
                    [0.1, 0.1, 0.1, 0.8, 0.1, 0.8],
                    [0, 0, 0, 0, 0, 0, 0, 0]], dtype=float)
    torch.from_numpy(data).cpu().cpu()
    return [torch.argmax(data, axis=-1)]



### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(y, f)
