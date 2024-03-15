import tensorflow as tf

labels = [0, 6, 5, 4, 2]

# Create a constant tensor with shape (len(labels), 10)
result = tf.constant(1, dtype=tf.int32, shape=[len(labels), 10])

# Iterate over the labels and set the corresponding indices to 0 in the result tensor
for i, label in enumerate(labels):
    result = tf.tensor_scatter_nd_update(result, [[i, label]], [0])

result