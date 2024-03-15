import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import numpy as np
import pandas as pd
import torch

x = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
### BEGIN SOLUTION
from scipy import ndimage.measurements




def get_data():
    return pd.DataFrame({
        "Index": list(range(6)), 
        "Value": ndimage.convolve(np.ones(6) * 2 - 1, x, mode="nearest").astype(int)
    })



### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(px, f)
