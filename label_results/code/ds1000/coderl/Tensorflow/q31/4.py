import tensorflow as tf


def f():
	xs = [tf.compat.as_bytes(b) for b in x]
	decode_X = tf.decode_bytes(xs, 'utf-8')
	return [decode_X.decode('utf-8')]
