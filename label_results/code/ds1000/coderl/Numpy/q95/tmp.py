import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
a = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
from itertools import groupby
from numpy import rolling_window




def sliding_window(a):
    l = len(a)
    return [[a[y:y+2*j, x:x+2*j] for j, i in enumerate(list(range(0,l)) + list(range(1,l)))] for x in range(0,l) for y in range(0,l)]



#print(result)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
