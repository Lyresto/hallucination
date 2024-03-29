import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
x = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))



def remove_nans(arr):
    arr = [i for i in arr if i!= np.nan]
    return arr



#print(x)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(x, file)
