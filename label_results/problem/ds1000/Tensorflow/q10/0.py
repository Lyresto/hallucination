max_len = 8
batch_size = len(lengths)

# Create a tensor of shape (batch_size, max_len) filled with 1s
mask = tf.ones((batch_size, max_len), dtype=tf.int32)

# Create a range tensor of shape (max_len,) with values from 0 to max_len-1
range_tensor = tf.range(max_len, dtype=tf.int32)

# Create a boolean mask of shape (batch_size, max_len) where True corresponds to indices less than the length
bool_mask = tf.math.less(range_tensor, tf.expand_dims(lengths, axis=1))

# Convert the boolean mask to integers (True -> 1, False -> 0)
int_mask = tf.cast(bool_mask, dtype=tf.int32)

# Invert the mask (1 -> 0, 0 -> 1)
inv_mask = tf.math.subtract(1, int_mask)

# Concatenate the inverted mask with the original mask along the second axis
result = tf.concat([inv_mask, int_mask], axis=1)
