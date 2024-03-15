from operator import itemgetter

def solve(a, b):
	c = []
	for x in range(len(a)):
		c.append([a[x][b[y][0]] for y in range(len(b))])
	return np.array(c)
