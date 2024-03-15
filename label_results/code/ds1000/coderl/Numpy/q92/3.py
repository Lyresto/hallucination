import numpy as np
result = np.array([0]*N)
for i in range(N):
	N -= 1
	result[i] = max(a[i:])
print(result)
