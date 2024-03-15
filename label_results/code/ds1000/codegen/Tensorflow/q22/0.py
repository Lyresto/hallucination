import tensorflow as tf

a = tf.constant([
  [1,1,1],
  [1,1,1]
])
b = tf.constant([
  [0,0,0],
  [1,1,1]
])

result = tf.reduce_sum(tf.square(a - b))
