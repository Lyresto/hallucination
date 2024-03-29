import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import tensorflow as tf

x,y,z = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
def f(x,y,z):
    ### BEGIN SOLUTION
    indices = tf.stack([y,z], axis=1)
    m = tf.gather_nd(x, indices)
    return m
    ### END SOLUTION
    
    print(f()) # Output: [2 6]
    
    
    ### END SOLUTION
result = f(x,y,z)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)