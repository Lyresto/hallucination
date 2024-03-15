import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import tensorflow as tf

lengths = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
import tensorflow as tf

lengths = [4, 3, 5, 2]

max_length = tf.reduce_max(lengths)
mask = tf.sequence_mask(lengths, max_length, dtype=tf.int32)
padding = tf.ones([len(lengths), max_length - tf.shape(mask)[1]], dtype=tf.int32)
result = tf.concat([mask, padding], axis=1)

result


###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)