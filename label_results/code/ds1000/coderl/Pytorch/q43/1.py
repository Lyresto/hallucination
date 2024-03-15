def max_prob(y, x):
	m = 0
	for i in range(len(x)):
		if y[i] == x[i]:
			m = m if m<0.5 else 0.5
	return m
