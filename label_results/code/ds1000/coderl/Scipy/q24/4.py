from collections import Counter
import scipy.spatial
import scipy.optimize

def manhattan(x1, x2):
	c1 = Counter(x1)
	c2 = Counter(x2)
	return sum((c1 - c2).values())

def match(x1, x2, n1, n2):
	# find the points that are in the first set
	idx1 = [i for i in range(n1) if x1[i] == x2[i]]
	if len(idx1) < 2:
		# no point in the first set
		return idx1
	# find the minimum distance between the 2 sets
	d1 = manhattan(x1, x2)
	d2 = manhattan(x1, x2[idx2[0]])
	# try to find the closest points to each other
	idx = scipy.optimize.bisect(idx1, idx2)
	return [idx - 1, idx]
