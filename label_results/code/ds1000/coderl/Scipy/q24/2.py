from collections import Counter

def manhattan(point1, point2):
	return sum((point1[i] - point2[i])**2 for i in range(len(point1)))**0.5

def find_best_match(points1, points2):
	point_to_value = dict()
	for i, point1 in enumerate(points1):
		for j, point2 in enumerate(points2):
			if point1 == point2:
				point_to_value[(i,j)] = i
	return point_to_value
