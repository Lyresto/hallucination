import numpy as np
from scipy.optimize import fsolve
def eqn(x, a, b):
	return x + 2*a - b**2

x0 = 0.5
fsolve(eqn, x0=x0, args=tuple([a,b]))
