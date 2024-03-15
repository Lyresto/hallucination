import numpy as np
a = np.array([[10,50,30],[60,20,40]])
a_new = a[0]
for i in range(len(a)):
	a_new[i] = np.ravel(a[i])
a_new.sort()
for i in range(len(a_new)):
	print(a_new[i])
