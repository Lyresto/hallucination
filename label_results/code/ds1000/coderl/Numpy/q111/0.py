import numpy as np
def sub2ind(size, subscripts, i, j):
	arr = np.full((size,), float(i * size + j))
	for k, r in enumerate(subscripts):
		arr[:, k] = (i - r) * (size - k) / size
	return round(sum(arr), 8)
