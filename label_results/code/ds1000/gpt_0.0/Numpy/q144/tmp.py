import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
a = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
a[1,:] = 0
a[:,0] = 0

#print(a)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(a, file)
