def mask(a):
	m, n = np.array(a).min(), len(a)
	return np.array([[i == m or i == n-1] for i in range(n)])
