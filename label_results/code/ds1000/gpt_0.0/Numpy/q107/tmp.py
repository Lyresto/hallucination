import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
import pandas as pd
A, a, b = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
B = pd.Series(index=A.index)
B[0] = a * A[0]
for t in range(1, len(A)):
    B[t] = a * A[t] + b * B[t-1]

#print(B)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(B, file)
