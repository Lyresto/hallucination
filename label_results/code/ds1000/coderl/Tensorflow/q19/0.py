import numpy as np
import tensorflow as tf

np.random.seed(10)
A = tf.constant(np.random.randint(100,size=(5, 3)))
sess = tf.Session()
np_sum = np.sum(A, axis=1)
res = sess.run(A)
print(np_sum)
