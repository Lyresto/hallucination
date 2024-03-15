from numpy import unpackbits
def matrix(a):
	m, n = len(a), len(a[0])
	return [unpackbits(a[i:i+m])[::-1] for i in range(0, n)]
