import tensorflow as tf

def f(x=example_x):
	# return the solution in this function
	return [tf.compat.decode_raw(s, 'utf-8') for s in x]
