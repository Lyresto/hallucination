import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
a = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
from itertools import groupby
from collections import Counter




def extract(a):
    c = Counter(tuple(l) for _, l in groupby(a))
    return [[tuple(b) for b in a[i:i+2*len(a)].T] for i in range(0, len(a), 2*len(a))]



#print(result)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
