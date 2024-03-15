import numpy as np
from scipy import interpolate as intp
x = []
y = []
def f(i,j):
	x.append(i);y.append(j);return (x[i]*y[j]+y[i]*x[j+1]-x[i]*y[j+1])/4
for i in range(2):
	for j in range(2):
		f(i,j)
print(f(0,1))
