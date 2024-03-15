import scipy.integrate
import numpy as np

def dN1_dt(t, N1):
    return -100 * N1 - np.cos(t)

N0 = 10
time_span = [-0.1, 0.1]

sol = scipy.integrate.solve_ivp(fun=dN1_dt, t_span=time_span, y0=[N0,], method='RK45')
result = sol.y