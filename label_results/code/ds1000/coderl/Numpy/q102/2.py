import numpy as np

a = np.array([[ 0,  1,  2,  3, 5, 6, 7, 8],
			 [ 4,  5,  6,  7, 5, 3, 2, 5],
			 [ 8,  9, 10, 11, 4, 5, 3, 5]])
l, r = 1, 10
result = []

while l <= r:
	c = a[:, l-1:r]
	res = [sum(i) for i in zip(*c)]
	if len(res) == 10:
		result.append(res[0:10])
		l += 1
	else:
		l += 1
		r -= 1
print(result)
