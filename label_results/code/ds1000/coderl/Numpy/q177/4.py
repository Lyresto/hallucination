from numpy import linspace, center

def rolling_window(a, size, center=0):
	L = len(a)
	return [array(a[b:b+size[0], c:c+size[1]]) for b in range(L-center) for c in range(L-center)]
