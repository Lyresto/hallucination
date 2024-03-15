import tensorflow as tf

x = [[[[1, 2, 3], [2, 3, 4], [0, 0, 0]],
      [[1, 2, 3], [2, 0, 4], [3, 4, 5]],
      [[1, 2, 3], [0, 0, 0], [0, 0, 0]],
      [[1, 2, 3], [1, 2, 3], [1, 2, 3]]]]
x = tf.convert_to_tensor(x, dtype=tf.float32)

y = tf.reduce_mean(x, axis=0)
