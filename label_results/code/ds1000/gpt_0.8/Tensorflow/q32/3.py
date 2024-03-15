result = tf.reduce_sum(x, axis=-2) / tf.math.count_nonzero(x, axis=-2, dtype=tf.float32)
