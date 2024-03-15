#!/usr/bin/env python3

def solve_linear(a, b, A):
	B = [a*A[0]]
	for i in range(1, len(A)):
		B.append(a*A[i] + b*B[i-1])
	return B

def solve_triangular(a, b, A):
	B = [a*A[0]]
	i = 1
	for j in range(1, len(A)):
		B.append(a*A[i] + b*B[j-1])
		i += 1
	return B

def solve_square(a, b, A):
	B = [a*A[0]]
	i = 1
	for j in range(1, len(A)):
		B.append(a*A[i] + b*B[j-1])
		i += 1
	return B

def solve_six(a, b, A):
	B = [a*A[0]]
	i = 1
	for j in range(1, len(A)):
		B.append(a*A[i] + b*B[j-1])
		i += 1
	return B

def solve_five(a, b, A):
	B = [a*A[0]]
	i = 1
	j = 1
	for k in range(1, len(A)):
		B.append(a*A[i] + b*B[j-k])
		i += 1
		j += k
	return B

def solve_five_square(a, b, A):
	B = [a*A[0]]
	i = 1
	j = 1
	k = 1
	for l in range(1, len(A)):
		B.append(a*A[i] + b*B[j-k])
		i += 1
		j += k
		k = k+1
	return B

def solve_nine(a, b, A):
	B = [a