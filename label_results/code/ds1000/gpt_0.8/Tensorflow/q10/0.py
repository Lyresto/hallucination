import tensorflow as tf

lengths = [4, 3, 5, 2]

max_length = tf.reduce_max(lengths)
mask = tf.sequence_mask(lengths, max_length, dtype=tf.int32)
padding = tf.ones([len(lengths), max_length - tf.shape(mask)[1]], dtype=tf.int32)
result = tf.concat([mask, padding], axis=1)

result