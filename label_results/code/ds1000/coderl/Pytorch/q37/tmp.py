import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import numpy as np
import pandas as pd
import torch

t, idx = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
### BEGIN SOLUTION
from itertools import chain, groupby
from numpy import array, sqrt, floor, ceil, copysign
from operator import mul




def load_data():
    t = array(list(map(float, input().split())))
    idx = list(chain.from_iterable([i-1 for i,_ in groupby(t)]))
    return t, idx



### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)
