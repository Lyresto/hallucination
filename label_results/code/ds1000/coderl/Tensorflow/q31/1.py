import tensorflow as tf
def f(x=example_x):
	return [str(tf.compat.bytes_to_string(tf.decode_binary(t))[0]) for t in x]
