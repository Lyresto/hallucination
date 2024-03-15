import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import tensorflow as tf

a,b = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
import tensorflow as tf

a = tf.constant([
  [1,1,1],
  [1,1,1]
])
b = tf.constant([
  [0,0,0],
  [1,1,1]
])

result = tf.reduce_sum(tf.square(a - b))

###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)