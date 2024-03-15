from itertools import zip_longest
from numpy import *

def sliding_window(a, window_size):
	arr = [[] for _ in range(window_size)]
	i, j = 0, 0
	while i < len(a) and j < len(a[0]):
		arr[i].extend(zip_longest(*[itertools.islice(a, j, i+2*window_size)] \
						  if i < len(a) else []))
		arr[j].extend(zip_longest(*[itertools.islice(a, i, j+2*window_size)] \
						  if j < len(a[0]) else []))
		i, j = i+window_size, j+window_size
	return arr
