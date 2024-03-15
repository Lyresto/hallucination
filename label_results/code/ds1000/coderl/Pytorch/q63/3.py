def solve(a, b):
	# your code here
	t = [list(zip(a[i][:-2] + b[i][:-2], a[i][1:]+b[i][1:])) for i in range(2)]
	return [list(map(mean,i)) for i,mean in zip(*t)]
	
def mean(t):
	return sum(t[0]) / len(t[0])
