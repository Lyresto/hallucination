import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import tensorflow as tf

seed_x = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
import tensorflow as tf

seed_x = 10
tf.random.set_seed(seed_x)
result = tf.random.uniform(shape=(114,), minval=2, maxval=6, dtype=tf.int32)

###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)