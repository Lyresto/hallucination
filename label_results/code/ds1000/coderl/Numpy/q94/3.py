import numpy as np

def extract(a):
	c = []
	for i in range(len(a)):
		for j in range(len(a[i])):
			temp = []
			temp = a[i][j::2] + a[i][1::2]
			temp = a[i][1::2] + a[i][::2]
			c.append(temp)
	return c
