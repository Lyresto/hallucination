import numpy as np
import tensorflow as tf
a = np.array([[1,1,1],[1,1,1]])
b = np.array([[0,0,0],[0,0,0]])

print(a)
print(b)
c = tf.square(a - b)
print(c)
res = c.reduce_sum()
print(res)
