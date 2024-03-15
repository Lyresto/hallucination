import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import tensorflow as tf

lengths = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))



def f(lengths):
    ### BEGIN SOLUTION
    import numpy as np
    
    
    


def f(lengths=example_lengths):
    L = np.array(lengths)
    return np.pad(L, 1, mode="constant").reshape(8, 8)



    ### END SOLUTION
result = f(lengths)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)