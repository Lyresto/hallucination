import tensorflow as tf

a = tf.constant([
  [1,1,1],
  [1,1,1]
])
b = tf.constant([
  [0,0,0],
  [1,1,1]
])

distances = tf.reduce_sum(tf.square(tf.subtract(a, b)), axis=1)
result = distances.numpy().tolist()
result