import numpy as np


def get_indices_of_the_N_biggest_elements_in_decreasing_order(a, N):
	arr = np.array(a)
	indices = []
	for i, n in enumerate(arr):
		if n == max(arr):
			indices.append(i)
	
	return indices
