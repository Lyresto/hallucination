result = tf.reduce_sum(x, axis=-2) / tf.reduce_sum(tf.cast(x != 0, dtype=tf.float32), axis=-2)
