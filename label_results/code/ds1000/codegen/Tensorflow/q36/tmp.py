import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import tensorflow as tf

a = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
import tensorflow as tf

a = tf.constant(
    [[0.3232, -0.2321, 0.2332, -0.1231, 0.2435, 0.6728],
     [0.2323, -0.1231, -0.5321, -0.1452, 0.5435, 0.1722],
     [0.9823, -0.1321, -0.6433, 0.1231, 0.023, 0.0711]]
)

result = tf.reduce_mean(a, axis=0)

###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)