from collections import Counter

def load_data():
	a = np.array([i for i in range(1000)], dtype = np.int64)
	b = np.array([i for i in range(1000)], dtype = np.int64)
	a, b = a.reshape(-1, 1), b.reshape(-1, 1)
	return a == b
	
def Count(a, b):
	c = Counter(a) == Counter(b)
	return c.sum()
