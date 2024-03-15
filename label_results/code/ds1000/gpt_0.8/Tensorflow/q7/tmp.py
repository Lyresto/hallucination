import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import tensorflow as tf

input = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
tf.compat.v1.disable_eager_execution()
###BEGIN SOLUTION
ds = tf.data.Dataset.from_tensor_slices(input)
ds = ds.flat_map(lambda x: tf.data.Dataset.from_tensor_slices(my_map_func(x)))
element = ds.make_one_shot_iterator().get_next()
result = []
with tf.compat.v1.Session() as sess:
    for _ in range(9):
        result.append(sess.run(element))



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)