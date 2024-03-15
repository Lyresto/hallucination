import tensorflow as tf
from tensorflow.python.framework import constant_op

def rand_tensor(shape, minval, maxval, seed):
	tf.set_random_seed(seed)
	return constant_op.constant(list(range(minval, maxval + 1)), shape=shape)
