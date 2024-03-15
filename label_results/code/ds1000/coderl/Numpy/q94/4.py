from itertools import zip_longest


def extract(arr):
	xs = zip_longest(*arr, fillvalue=0)
	return [[xs[i][j:j+2] for i in range(len(arr)) for j in range(2 * len(arr[i]))] for x in arr for y in x for z in y]
