import scipy.integrate
import numpy as np

def dN1_dt_simple(t, N1):
	return -100 * N1

def solve_ivp(fun, t_span, y0):
	print(fun, t_span, y0)
	time_span = np.array(t_span)
	return scipy.integrate.odeint(fun, [0]*len(time_span), t0=N0, args=y0)
