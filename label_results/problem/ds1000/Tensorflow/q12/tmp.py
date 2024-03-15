import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import tensorflow as tf

lengths = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
def f(lengths):
    ### BEGIN SOLUTION
    max_length = 8
    batch_size = len(lengths)
    
    # Create a tensor of shape (batch_size, max_length) filled with zeros
    mask = tf.zeros((batch_size, max_length), dtype=tf.int32)
    
    # Loop through each sequence length and set the corresponding values in the mask to 1
    for i, length in enumerate(lengths):
        mask[i, :length] = tf.ones((length,), dtype=tf.int32)
    
    return mask
    ### END SOLUTION
    
    
    ### END SOLUTION
result = f(lengths)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)