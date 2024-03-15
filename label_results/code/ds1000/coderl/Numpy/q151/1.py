import numpy as np
A = np.array([1,1,2,3,3,3,4,5,6,7,8,8])
B = np.array([1,2,8])
C = np.array([3,3,3,4,5,6,7])
for i in range(0,len(B)):
	if B[i] in A:
		A = A[A.index(B[i])+1:]
	else:
		C = C[1:] + A

