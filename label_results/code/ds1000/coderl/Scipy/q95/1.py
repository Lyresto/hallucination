import numpy as np
from scipy.optimize import fsolve

def eqn(x, a, b):
	return x + 2*a - b**2

def root(eqn, x0, args):
	fsol = fsolve(eqn, x0=x0, args=args)
	return fsol[0] if fsol[0] > 0 else -1*fsol[1]
