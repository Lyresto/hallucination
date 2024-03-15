max_length = 8
batch_size = len(lengths)

# Create a tensor of shape (batch_size, max_length) filled with zeros
mask = tf.zeros((batch_size, max_length), dtype=tf.int32)

# Loop through each sequence length and set the corresponding values in the mask to 1
for i, length in enumerate(lengths):
    mask[i, :length] = tf.ones((length,), dtype=tf.int32)

return mask
### END SOLUTION