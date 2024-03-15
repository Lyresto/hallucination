def anderson(x1, x2):
	p = [i/20 for i in range(len(x1))]
	a = [ss.average_difference(x1[i], x2[i]) for i in range(len(x1))]
	return (sum(a) == (len(x1)-len(x2))/2) and p == list(p)
