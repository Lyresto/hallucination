import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
A, B = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
from numpy import remove

a, b = list(map(float, input().split()))
c = remove(a, b)



#print(C)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(C, file)
