import numpy as np

# tf.reduce_sum doesn't allow to reduce by row
def dist(a,b):
	return np.sqrt(np.sub(a,b))**2

# what I want to do is calculate the L2 distance d(A,B) element-wise. 
# First I did a tf.sub(lhs, rhs) to get
[
[1,1,1],
[0,0,0],
[1,1,1]
]
# and then I want to do an element-wise reduce which returns 
[
3,
  0
]

