import tensorflow as tf

lengths = [4, 3, 5, 2]

max_length = max(lengths)
batch_size = len(lengths)

mask = tf.sequence_mask(lengths, maxlen=max_length, dtype=tf.int32)
padding = tf.ones((batch_size, max_length - tf.shape(mask)[1]), dtype=tf.int32)
result = tf.concat([mask, padding], axis=1)
result = tf.cast(result, dtype=tf.int32)
result