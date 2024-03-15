import tensorflow as tf

lengths = [4, 3, 5, 2]
max_length = 8

mask = tf.sequence_mask(lengths, maxlen=max_length, dtype=tf.int32)
padding = tf.ones([len(lengths), max_length - tf.reduce_max(lengths)], dtype=tf.int32)
result = tf.concat([mask, padding], axis=1)
