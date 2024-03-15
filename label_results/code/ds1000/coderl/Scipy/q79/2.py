import scipy.integrate
import numpy as np
def dN1_dt_simple(t, N1):
	return -100 * N1

def solve_ivp(fun, t_span, y0, args=None):
	import pandas as pd
	if args is None: args = []
	s = scipy.integrate.ode(fun, y0, args=args)
	return s.y
