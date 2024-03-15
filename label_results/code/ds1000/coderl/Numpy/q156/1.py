def f(a=example_a):
	l=len(a)
	x=sorted(a,reverse=True)
	return [x[i]*(-1)**(l-i-1) for i in range(l)]
