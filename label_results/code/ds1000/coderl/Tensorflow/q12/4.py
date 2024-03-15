from functools import reduce

def f(lengths=example_lengths):
	return tf.reduce_sum(lengths) & ~tf.reduce_sum(lengths)
