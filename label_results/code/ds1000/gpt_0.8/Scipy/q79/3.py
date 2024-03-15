from scipy.integrate import solve_ivp
import numpy as np

def dN1_dt(t, N1):
    return -100 * N1 - np.cos(t)

sol = solve_ivp(fun=dN1_dt, t_span=time_span, y0=[N0,])
result = sol.y