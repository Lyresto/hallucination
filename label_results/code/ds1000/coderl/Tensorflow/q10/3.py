import tensorflow as tf

def mask_tensor(lengths):
	return [tf.zeros((8, len(lengths)), dtype=tf.int32) for _ in lengths]
