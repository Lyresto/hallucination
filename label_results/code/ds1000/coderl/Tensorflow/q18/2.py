import tensorflow as tf
a = tf.constant(np.random.rand(50, 100, 512))
with tf.Session() as sess:
	print(sess.run(a))
