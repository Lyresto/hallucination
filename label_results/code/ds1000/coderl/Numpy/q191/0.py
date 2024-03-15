import numpy as np
def hypot(x1, x2):
	return (x1 ** 2 + x2 ** 2) ** 0.5

def solve2d(x, y):
	f = lambda x: x ** 2 + x * y + x
	xs = sorted([x, y])
	l = [0, f(xs[0])]
	for i in range(1, len(xs) - 1):
		f = f(xs[i])
		t = xs[i + 1] - xs[i]
		k = f(t)
		if k < l[0]:
			l[0], l[1], l[2] = k, t, k
	return l

def solve3d(x, y):
	f = lambda x: x ** 2 + x * y + x
	xs = sorted([x, y])
	for i in range(1, len(x) - 1):
		f = f(xs[i])
		t = xs[i + 1] - xs[i]
		k = f(t)
		if k < l[1]:
			l[1], l[2] = k, t, k
	return l

def solve(x, y):
	res = solve3d(x, y)
	mn = res[0]
	mx = res[1]
	k = res[2]
	diff = mx - mn
	for i in range(3):
		if diff < k:
			mn = res[i]
			diff = k - mn
	return [mn, diff, mx]

def solve2(x, y):
	res = solve(x, y)
	mn = res[0]
	mx = res[1]
	k = res[2]
	diff = mx - mn
	for i in range(3):
		if diff < k:
			mn = res[i]
			diff = k - mn
	return [mn, diff, mx]






#BEGIN SOLUTION
import numpy as np
x = [-1, 2, 5, 100