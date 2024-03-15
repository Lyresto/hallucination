from numpy import dot, dot

def sub2ind(n, k, i, j):
	return dot(n,(i - j + 1,j - k + 1)) / dot(n, n)
