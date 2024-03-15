import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import tensorflow as tf

labels = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
import tensorflow as tf

labels = [0, 6, 5, 4, 2]

# Create a tensor of shape (len(labels), 10) with all ones
ones_tensor = tf.ones((len(labels), 10), dtype=tf.int32)

# Create a tensor of shape (len(labels), 10) with all zeros
zeros_tensor = tf.zeros((len(labels), 10), dtype=tf.int32)

# Create a tensor of shape (len(labels), 10) with ones at the specified indices
result = tf.tensor_scatter_nd_update(zeros_tensor, tf.expand_dims(tf.range(len(labels)), axis=1), ones_tensor)

result


###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)