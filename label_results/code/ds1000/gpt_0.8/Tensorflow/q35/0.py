import tensorflow as tf
tf.random.set_seed(10)
A = tf.random.normal([100,100])
B = tf.random.normal([100,100])
result = tf.reduce_sum(tf.matmul(A,B)).numpy()
