import numpy as np
x = np.array([0, 1, 1, 1, 3, 1, 5, 5, 5])
y = np.array([0, 2, 3, 4, 2, 4, 3, 4, 5])
c=[]
for i in range(len(x)):
	for j in range(len(y)):
		if x[i]==y[j]:
			c.append([i,j])
c=sorted(c,key=lambda x:x[0])
for i in c:
	if i[1]==0:
		print(i[0])
		break
