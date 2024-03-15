def solve(a, b):
	# return the solution in this function
	a = [list(i) for i in a]
	b = [list(i) for i in b]
	x = [0]*len(a[0])
	y = [0]*len(a[0])
	z = [0]*len(a[0])
	a_s = sum(a[-1])
	b_s = sum(b[-1])
	for i in range(len(a)):
		x[i] = a_s/len(a[i]) if a_s>0 else 0
		y[i] = b_s/len(b[i]) if b_s>0 else 0
		z[i] = x[i]+y[i]+z[i]
	return [x+y+z]
