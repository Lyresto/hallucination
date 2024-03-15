import numpy as np
def uniform(min,max,n):
	res = np.random.uniform(min,max,n)
	return res.astype("i")
