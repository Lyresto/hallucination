from numpy import linspace as u
from scipy import interpolate as i

def interpolate_2d(x, y, a):
	return i.interp2d(x, y, a)([u(x), u(y)], [0, 0])[0]
