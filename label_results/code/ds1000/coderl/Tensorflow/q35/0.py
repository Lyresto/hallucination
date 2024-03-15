import tensorflow as tf

sess = tf.Session()
a = tf.constant([1,2,3,4,5])
b = tf.constant([6,7,8,9,10])

print(sess.run(a+b))
