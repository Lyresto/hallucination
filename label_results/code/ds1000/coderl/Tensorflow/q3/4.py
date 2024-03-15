from collections import Counter

def metric_score(labels, scores):
	return (sum(y == x for x, y in zip(labels, scores)) / len(labels) * 10, Counter(labels))
