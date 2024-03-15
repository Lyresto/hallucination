import numpy as np
np.random.seed(10)
A = tf.constant(np.random.randint(100,size=(5,3)))
sess = tf.Session()
print((np.sum(A, axis=1)))
