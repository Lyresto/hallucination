import tensorflow as tf

labels = [0, 6, 5, 4, 2]

# Create a tensor with shape (len(labels), 10) filled with ones
result = tf.ones((len(labels), 10), dtype=tf.int32)

# Set the values at the indices specified by labels to zero
result = tf.tensor_scatter_nd_update(result, tf.expand_dims(labels, axis=1), tf.zeros(len(labels), dtype=tf.int32))

result