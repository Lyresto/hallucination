import numpy as np

def zero_out_first_and_second(a):
	for i in range(len(a[0])):
		if a[0][i] == 0:
			a[1][i] = 0
	for j in range(len(a)):
		if a[0][j] == 0:
			a[0][j] = 0

def zero_out_last_row(a):
	for i in range(len(a)):
		if a[-1][i] == 0:
			a[-1][i] = 0

def zero_out_first_col(a):
	for j in range(len(a[0])):
		if a[0][j] == 0:
			a[0][j] = 0

def zero_out_second_col(a):
	for i in range(len(a)):
		if a[i][0] == 0:
			a[i][0] = 0

#I could do this in O(n*m) but it's not easy
def zero_out_all_cols(a):
	for i in range(len(a[0])):
		a[i][0] = 0

#END SOLUTION
