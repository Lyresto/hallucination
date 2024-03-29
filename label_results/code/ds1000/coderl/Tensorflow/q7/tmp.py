import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import tensorflow as tf

input = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
tf.compat.v1.disable_eager_execution()
###BEGIN SOLUTION
import tensorflow as tf
ds = tf.data.Dataset.from_tensor_slices([0, 0, 0])
ds = ds.map(lambda x: [i for i in range(x)])
element = ds.make_one_shot_iterator().get_next()
result =... # put solution in this variable



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)