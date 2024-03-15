import numpy as np
from scipy import interpolate as intp
x = []
y = []
for i in range(0,100):
	for j in range(0,100):
		x.append(i*2+j)
		y.append(j*2+i)
interp = intp.interp2d(x,y,a)
print(interp(0,0))
