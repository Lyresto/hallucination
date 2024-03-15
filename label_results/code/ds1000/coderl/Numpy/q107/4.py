#!/usr/bin/env python3

import pandas as pd

def solve(a, b):
	if a == 0 and b == 0:
		return 0
	B = [None] * len(A)
	B[0] = a*A[0]
	p = 1
	while p < len(A):
		B[p] = a*A[p] + b*B[p-1]
		p += 1
	return B

def __starting_point():
	print(solve(1, 2))
__starting_point()
