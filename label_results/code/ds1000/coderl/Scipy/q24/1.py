from collections import Counter
from scipy.spatial import ConvexHull

def manhattan(p1, p2):
	return sum((p1[i] - p2[i]) ** 2 for i in range(len(p1)))

def find_matched(p1, p2, i0, i1, k):
	c1, c2 = p1[i0], p2[i1]
	hull = ConvexHull(n=k)
	for j in range(k):
		hull.filter.append([c1[j], c2[j]])
	matched = [i for i, (x, y) in enumerate(hull.kmeans(k)[1]) if x!= y]
	return matched
