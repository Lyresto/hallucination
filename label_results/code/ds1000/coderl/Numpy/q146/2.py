from numpy import min

def mask(a):
	m, n = min(a), max(a)
	return np.array([[i == m or i == n] for i in range(a.shape[0])])
