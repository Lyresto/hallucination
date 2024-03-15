import numpy as np

def sliding_window(a):
	n,m = len(a), len(a[0])
	return [[[(a[b][c] - a[b][c+1])/2 + (a[b][c] - a[b][c+1])/2 for c in range(0,m-1)] for b in range(0,n-1)]
