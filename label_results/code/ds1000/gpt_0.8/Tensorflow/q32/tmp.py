import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import tensorflow as tf

x = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
sum_values = tf.reduce_sum(x, axis=-2) # sum along second to last dimension
non_zero_entries = tf.math.count_nonzero(x, axis=-2, keepdims=True) # count non-zero entries
result = sum_values / non_zero_entries # divide sum by number of non-zero entries



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)