import tensorflow as tf

def accuracy(a):
	return tf.reduce_mean(tf.cast(a, "float")) == sum(y == x for x, y in zip(a, a[1:])) / 10
