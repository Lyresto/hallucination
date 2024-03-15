def f(a=example_a):
	# your code here
		d = np.array([(a.count(i),i) for i in set(a)])
		return sorted(d, reverse=True)[0][1]
