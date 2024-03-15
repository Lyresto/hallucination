import numpy as np
A = np.array([1,1,2,3,3,3,4,5,6,7,8,8])
B = np.array([1,2,8])
C = np.array([3,3,3,4,5,6,7])
B.sort()
for i in range(0,len(B)):
	if B[i] in A:
		A = np.delete(A,B[i])
	C = np.insert(C,B[i],1)
