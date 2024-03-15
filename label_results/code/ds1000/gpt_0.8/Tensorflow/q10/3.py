import tensorflow as tf

lengths = [4, 3, 5, 2]

# Get the maximum length
max_length = tf.reduce_max(lengths)

# Create a mask tensor with 1s and 0s
mask = tf.sequence_mask(lengths, maxlen=max_length, dtype=tf.int32)

# Pad the mask tensor with 1s
padded_mask = tf.pad(mask, [[0, 0], [0, max_length - tf.shape(mask)[1]]], constant_values=1)

result = padded_mask
