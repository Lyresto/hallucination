import scipy.integrate
import numpy as np

N0 = 10
time_span = [-0.1, 0.1]

def dN1_dt_time_varying(t, N1):
    return -100 * N1 - np.cos(t)

sol = scipy.integrate.solve_ivp(fun=dN1_dt_time_varying, t_span=time_span, y0=[N0,])
result = sol.y
result