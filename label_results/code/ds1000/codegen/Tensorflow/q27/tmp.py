import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import tensorflow as tf

x,y,z = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
def f(x,y,z):
    ### BEGIN SOLUTION

    result = tf.matmul(x,y,z)
    ### END SOLUTION
    return result

f(x,y,z)

    ### END SOLUTION
result = f(x,y,z)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)