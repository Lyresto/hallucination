import numpy as np
from scipy.optimize import fsolve
def eqn(x, a, b):
	return x + 2 * a - b**2
fsolve(eqn, x0=0.5, args = (a,b))
