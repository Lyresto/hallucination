import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import tensorflow as tf
import numpy as np

A = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
import numpy as np
import tensorflow as tf

np.random.seed(10)
A = tf.constant(np.random.randint(100,size=(5, 3)))
sess = tf.Session()
np_sum = np.sum(A, axis=1)
res = sess.run(A)
print(np_sum)



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)