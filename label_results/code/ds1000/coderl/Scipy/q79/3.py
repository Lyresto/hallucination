import scipy.integrate
import numpy as np
def dN1_dt_simple(t, N1):
	return -100 * N1

def solve_ivp(fun, t_span, y0):
	t = np.array(t_span)
	sol = scipy.integrate.odeint(fun, y0, t)
	return sol.y
