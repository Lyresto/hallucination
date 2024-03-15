import numpy as np
import tensorflow as tf
np.random.seed(10)
A = tf.constant(np.random.randint(100,size=(5, 3)))
res = np.sum(A, axis=1)
