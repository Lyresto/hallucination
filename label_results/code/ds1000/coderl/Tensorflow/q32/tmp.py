import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import tensorflow as tf

x = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
import numpy as np





def find_space_average(x):
    s = np.mean(np.array(x[0][0]), axis=-1)
    nz = len([i for i in x[0][0] if i!= 0])
    return [s / nz for i in range(len(s))]



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)