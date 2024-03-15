import tensorflow as tf

labels = [0, 6, 5, 4, 2]

# Create a tensor of shape (len(labels), 10) with all ones
ones_tensor = tf.ones((len(labels), 10), dtype=tf.int32)

# Create a tensor of shape (len(labels), 10) with all zeros
zeros_tensor = tf.zeros((len(labels), 10), dtype=tf.int32)

# Create a tensor of shape (len(labels), 10) with ones at the specified indices
result = tf.tensor_scatter_nd_update(zeros_tensor, tf.expand_dims(tf.range(len(labels)), axis=1), ones_tensor)

result