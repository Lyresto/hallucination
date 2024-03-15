import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import tensorflow as tf

x,y,z = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))



def f(x,y,z):
    ### BEGIN SOLUTION
    import numpy as np
    


def f(x=example_x,y=example_y,z=example_z):
     ### START SOLUTION
    np_arr = np.array(x)
    return np_arr[y,z]



    ### END SOLUTION
result = f(x,y,z)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)