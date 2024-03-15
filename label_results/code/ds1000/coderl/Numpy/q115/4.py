def fast_solution(a, index):
	max_so_far = a[index.size]
	for i in range(index.size):
		if a[i] > max_so_far:
			max_so_far = a[i]
	return max_so_far
