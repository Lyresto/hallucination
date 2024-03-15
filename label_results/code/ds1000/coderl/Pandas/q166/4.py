def stdMeann(x):
	m, s = 0, 0
	for i in x:
		m += i
		s += i**2
	return s/len(x)
