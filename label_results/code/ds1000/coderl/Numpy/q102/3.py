import numpy as np

a = np.array([[ 0,  1,  2,  3, 5, 6, 7, 8],
			 [ 4,  5,  6,  7, 5, 3, 2, 5],
			 [ 8,  9, 10, 11, 4, 5, 3, 5]])

ret = a[:, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]

for i in range(1, 11):
	b = a[:, [i, i + 1]]
	if low <= len(b) - 1 and high >= len(b[0]) - 1:
		low += 1
		high -= 1
	elif low > len(b) - 1 and high <= len(b[0]) - 1:
		break
	else:
		continue
	
	ret = np.concatenate((ret, b), axis=1)

print(ret)
