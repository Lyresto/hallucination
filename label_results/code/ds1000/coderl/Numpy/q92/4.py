import numpy as np

def get_indexes_of_the_N_biggest_elements_in_decreasing_order(a, N):
	b = np.array(a)
	c = b.copy()
	for i in range(1, N+1):
		c[i] = c[i-1]
		if c[i] > b[i]:
			c[i] = b[i]
	return c
