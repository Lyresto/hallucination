import numpy as np


def dist(a, b):
	a = np.expand_dims(a, axis=0)
	b = np.expand_dims(b, axis=0)
	return np.sqrt(np.sub(a, b))

print((dist([[1,1,1], [1,1,1]])))
print((dist([[0,0,0], [1,1,1]]), 3))
