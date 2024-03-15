import numpy as np

import tensorflow as tf

np.random.seed(10)
a = tf.constant(np.random.rand(50, 100, 512))
with tf.Session() as sess:
	s = sess.run(a)
	print(s)
