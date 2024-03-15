import numpy as np
A = np.array([1,1,2,3,3,3,4,5,6,7,8,8])
B = np.array([1,2,8])
C = np.array([3,3,3,4,5,6,7])
for i in range(0,len(B)):
	for j in range(0,len(A)):
		if B[i] in A:
			A.remove(B[i])
			C = C.append(3)
print(C)
