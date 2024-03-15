def load_data():
	t = list(map(float, input().split()))
	idx = [i for i, x in enumerate(t)]
	return t, idx
