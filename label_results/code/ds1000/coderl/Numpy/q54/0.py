import numpy as np

def solve():
	col = int(input())
	a = list(map(float, input().split()))
	mult = a[col]
	c = 0
	s = []
	for i in range(len(a)):
		c += a[i]
		s.append(c)
	result = s
	print(result)

def __starting_point():
	solve()
__starting_point()
