def fast_solution(a, index):
	return [max(a[i] for i in index) for i in range(len(a))]
