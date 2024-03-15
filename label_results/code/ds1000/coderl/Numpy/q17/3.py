import numpy as np
r_old, r_new = np.random.randint(3, size=(100, 2000)) - 1 # put solution in these variables

def shuffle_it(r):
	np.random.shuffle(r)
	return r
