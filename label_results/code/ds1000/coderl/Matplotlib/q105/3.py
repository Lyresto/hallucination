def plot(x):
	cutoff = 0.01
	l = [cutoff for i in range(3)]
	l.append(cutoff)
	l[2] = 'cutoff'
	x = sorted(x)
	y = [i for i in range(len(l)) if x[i]==3]
	for j, i in enumerate(y):
		if j==0:
			plt.plot(x, l[i], '-', color='r', label='cutoff')
		else:
			plt.plot(x, l[i], '--', color='b', label='cutoff')
	plt.legend()
	
plot(range(3))
