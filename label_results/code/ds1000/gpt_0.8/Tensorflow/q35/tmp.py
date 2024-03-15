import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import tensorflow as tf

FLAG = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
import tensorflow as tf
tf.random.set_seed(10)
A = tf.random.normal([100,100])
B = tf.random.normal([100,100])
result = tf.reduce_sum(tf.matmul(A,B)).numpy()



###END SOLUTION
result = result.numpy()

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)