import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import tensorflow as tf
import numpy as np

a = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
result = tf.expand_dims(tf.expand_dims(a, 0), 3)



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)