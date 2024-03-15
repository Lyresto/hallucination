def get_distance_2(y, x):
	#your code here
	a,b,c,d = [],[],[],[]
	for i in range(6):
		for j in range(6):
			a.append(sum((y[i,j]-x[i,j])**2))
	for i in range(6):
		for j in range(6):
			c.append(sum((y[i,j]-x[i,j])**2))
	for i in range(6):
		for j in range(6):
			d.append(sum((y[i,j]-x[i,j])**2))
	return a,b,c,d
