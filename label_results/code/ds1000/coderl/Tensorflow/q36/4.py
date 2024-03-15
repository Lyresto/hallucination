from collections import Counter
from operator import itemgetter

def accuracy(scores):
	return float(sum(count[1] == value[1] for value, count in Counter(scores.numpy()).items())) / len(set(scores.numpy()))
