import tensorflow as tf
sess = tf.compat.v1.Session()
with sess:
	print(sess.run(tf.reduce_sum(tf.matmul(2, 3))))
