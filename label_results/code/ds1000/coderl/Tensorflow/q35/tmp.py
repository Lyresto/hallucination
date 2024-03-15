import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import tensorflow as tf

FLAG = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
import tensorflow as tf

sess = tf.Session()
a = tf.constant([1,2,3,4,5])
b = tf.constant([6,7,8,9,10])

print(sess.run(a+b))



###END SOLUTION
result = result.numpy()

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)