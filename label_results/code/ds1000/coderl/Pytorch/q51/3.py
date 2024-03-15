from collections import Counter

def load_data():
	a = np.array([i for i in range(1, 1001)])
	b = np.array([i for i in range(1, 1001)])
	a, b = torch.from_numpy(a), torch.from_numpy(b)
	return Counter(a), Counter(b)
