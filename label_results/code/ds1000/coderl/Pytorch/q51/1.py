def Count(A, B):
	a = list(map(int, A.numpy()))
	b = list(map(int, B.numpy()))
	counter_a = sum(a == b)
	return counter_a
