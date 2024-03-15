def load_data():
	t = tuple(map(float, input().split()))
	idx = tuple(map(int, input().split()))
	return [list(t[i]) for i in idx], idx
