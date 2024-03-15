from scipy.integrate import solve_ivp
import numpy as np

def dN1_dt_simple(t, N1):
	return -100 * N1

def solve_ivp(fun, t_span, y0):
	sol = solve_ivp(fun, t_span, y0)
	return sol.y
