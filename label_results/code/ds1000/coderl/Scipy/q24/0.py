from collections import Counter
from scipy.spatial import distance

def manhattan(p1, p2):
	return sum((p1[k] - p2[k]) ** 2 for k in range(p1.shape[0])) ** 0.5

def match(points1, points2):
	dists = [manhattan(points1[i], points2[i]) for i in range(len(points1))]
	return [k for k, d in enumerate(dists) if d == min(dists)]
