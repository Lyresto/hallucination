import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
x_dists, y_dists = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
from itertools import zip_longest




def dist(a, b):
    return sum(b[i][j] - a[i][j] for i in range(len(a)) for j in range(len(a[i])))**0.5




def permutate(arrays):
    return list(zip_longest(*arrays, fillvalue=0))



#print(dists)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(dists, file)
