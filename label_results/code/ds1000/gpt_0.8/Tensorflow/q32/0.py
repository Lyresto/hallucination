sum_values = tf.reduce_sum(x, axis=-2) # sum along second to last dimension
non_zero_entries = tf.math.count_nonzero(x, axis=-2, keepdims=True) # count non-zero entries
result = sum_values / non_zero_entries # divide sum by number of non-zero entries
