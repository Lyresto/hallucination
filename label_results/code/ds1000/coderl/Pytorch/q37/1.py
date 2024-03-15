from itertools import chain, groupby

def load_data():
	t = list(map(float, input().split()))
	idx = list(chain.from_iterable((i,) for i in range(len(t))))
	return t, idx
