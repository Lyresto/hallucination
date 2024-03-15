import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import tensorflow as tf

x = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
import tensorflow as tf

x = [[[[1, 2, 3], [2, 3, 4], [0, 0, 0]],
      [[1, 2, 3], [2, 0, 4], [3, 4, 5]],
      [[1, 2, 3], [0, 0, 0], [0, 0, 0]],
      [[1, 2, 3], [1, 2, 3], [1, 2, 3]]]]
x = tf.convert_to_tensor(x, dtype=tf.float32)

y = tf.reduce_mean(x, axis=0)

###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)