non_zero_entries = tf.math.count_nonzero(x, axis=-1)
sum_non_zero = tf.reduce_sum(x, axis=-2)
result = sum_non_zero / non_zero_entries