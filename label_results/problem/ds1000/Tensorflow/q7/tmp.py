import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import tensorflow as tf

input = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
tf.compat.v1.disable_eager_execution()
###BEGIN SOLUTION
def my_map_func(i):
    return [i, i+1, i+2]
ds = tf.data.Dataset.from_tensor_slices(input)
ds = ds.interleave(lambda x: tf.data.Dataset.from_tensor_slices(my_map_func(x)), cycle_length=len(input), num_parallel_calls=tf.data.experimental.AUTOTUNE)
result = list(ds.as_numpy_iterator())



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)