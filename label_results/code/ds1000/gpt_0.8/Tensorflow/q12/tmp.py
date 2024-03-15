import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import tensorflow as tf

lengths = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))



def f(lengths):
    ### BEGIN SOLUTION



def f(lengths=example_lengths):
    max_length = max(lengths)
    mask = tf.sequence_mask(lengths, max_length, dtype=tf.int32)
    padded_mask = tf.pad(mask, [[0, 0], [0, max_length - tf.shape(mask)[1]]])
    return padded_mask



    ### END SOLUTION
result = f(lengths)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)