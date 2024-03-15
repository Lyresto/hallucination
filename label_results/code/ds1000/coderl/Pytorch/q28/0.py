from itertools import chain

def tenzor_tensor(a, lengths):
	t = [[0] * len(a[0]) for _ in range(len(a))]
	for b, c in zip(a, lengths):
		t[b // len(a[0])][c // len(a[0])] = 1
	return chain.from_iterable(t)
