import numpy as np

np.random.seed(10)
a = tf.constant(np.random.rand(50, 100, 512))
res = a.reshape(1, 50, 100, 1, 512)
print(res.shape)
