import tensorflow as tf

def f():
	decoder = tf.pywrap_tensorflow(decode_bytes=lambda x: [chr(c) for c in x])
	return decoder.decode_bytes(x)
