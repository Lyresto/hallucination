import tensorflow as tf

seed_x = 10
tf.random.set_seed(seed_x)

result = tf.random.uniform([114], minval=2, maxval=6, dtype=tf.int32)