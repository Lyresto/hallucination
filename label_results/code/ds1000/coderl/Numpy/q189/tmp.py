import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
x, y, a, b = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
from numpy import *
a,b=map(int,input().split())
c=len(x)
d=len(y)
for i in range(c):
    if x[i]==a and y[i]==b:
        print(i)
        break



#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
