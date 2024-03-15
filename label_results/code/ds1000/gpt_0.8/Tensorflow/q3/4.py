import tensorflow as tf

labels = [0, 6, 5, 4, 2]

# Create a tensor with shape (len(labels), 10) filled with zeros
result = tf.zeros((len(labels), 10), dtype=tf.int32)

# Update the tensor at the corresponding indices with ones
for i, label in enumerate(labels):
    result[i, label] = 1
