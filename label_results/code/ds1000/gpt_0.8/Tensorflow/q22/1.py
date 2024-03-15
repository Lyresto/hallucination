import tensorflow as tf

a = tf.constant([
  [1,1,1],
  [1,1,1]
])
b = tf.constant([
  [0,0,0],
  [1,1,1]
])

# Calculate squared difference
squared_diff = tf.square(tf.subtract(a, b))

# Sum the squared differences along the rows
result = tf.reduce_sum(squared_diff, axis=1)
END SOLUTION