import tensorflow as tf

labels = [0, 6, 5, 4, 2]
one_hot_labels = tf.one_hot(labels, depth=10, dtype=tf.int32)
result = tf.tile(tf.expand_dims(one_hot_labels, axis=1), [1, 10, 1])
result