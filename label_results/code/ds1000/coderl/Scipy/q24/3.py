def manhattan(point1, point2):
	return sum((point1[i] - point2[i])**2 for i in range(len(point1))), points1.index(point1), points2.index(point2)

def find_best_match(points1, points2):
	n, k = len(points1), len(points2)
	dist1, idx1 = manhattan(points1, points2[:n//2])
	dist2, idx2 = manhattan(points1[idx1:], points2[idx1:k//2])
	return [idx2[i] for i in range(k) if dist1[i] < dist2[i]]
