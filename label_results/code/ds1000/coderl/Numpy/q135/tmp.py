import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
a, m = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
from numpy import unpackbits



def matrix(a):
    m, n = len(a), len(a[0])
    return [unpackbits(a[i:i+m])[::-1] for i in range(0, n)]



#print(result)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
