def mask(a):
	a_min = np.min(a, axis=1)
	return np.array([[i[axis] for i in a] for axis in range(a.shape[1])])[a_min == 0]
