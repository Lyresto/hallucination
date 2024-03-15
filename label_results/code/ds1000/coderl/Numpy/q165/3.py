def distance(a):
	n, m = len(a), len(a[0])
	return [[abs(x - y) for y in a] for x in range(n)]
