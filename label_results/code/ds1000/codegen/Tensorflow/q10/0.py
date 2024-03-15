lengths = tf.constant(lengths)
result = tf.pad(lengths, [[0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0]])
