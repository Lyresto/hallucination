def distance(a):
	n, m = len(a), len(a[0])
	dist = [[0] * m for i in range(n)]
	for i in range(n):
		for j in range(m):
			dist[i][j] = dist[i][a[i][j]] = (a[i][j] - a[i][a[j]][j]) ** 0.5
	return dist

def clustering(a):
	dist = distance(a)
	dist = [dist[i][j] for i in range(len(dist)) for j in range(i + 1, len(dist))]
	dist = np.array(dist)
	return dist.T
