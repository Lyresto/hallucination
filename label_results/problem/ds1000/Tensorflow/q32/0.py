# First, we need to count the number of non-zero entries in the second to last dimension
num_nonzero = tf.math.count_nonzero(x, axis=-2, dtype=tf.float32)

# Next, we need to set the zero entries to 1 to avoid division by zero
mask = tf.cast(tf.not_equal(num_nonzero, 0), dtype=tf.float32)
num_nonzero += mask

# Now, we can calculate the sum of the non-zero entries
sum_nonzero = tf.reduce_sum(x, axis=-2)

# Finally, we can divide the sum by the number of non-zero entries
result = sum_nonzero / num_nonzero

# Apply the mask to set the zero entries to 0
result *= mask
