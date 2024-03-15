def get_one_maximal_set_of_linearly_independent_vectors(a):
	m, n = len(a), len(a[0])
	V = [[0] * n for _ in range(m)]
	for j in range(n):
		for i in range(m):
			if a[i][j] == 1:
				V[i][j] = a[i][j]
				for k in range(j + 1, n):
					if a[i][k] == 1:
						V[i][j] = max(V[i][j], V[i][k] + V[k][j])
	return max(V[i][:j] for i in range(m))
