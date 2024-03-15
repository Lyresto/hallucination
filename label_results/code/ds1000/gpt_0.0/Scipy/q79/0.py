def dN1_dt(t, N1):
    return -100 * N1 + np.cos(t)

sol = scipy.integrate.solve_ivp(fun=dN1_dt, t_span=time_span, y0=[N0,], dense_output=True)

t_eval = np.linspace(time_span[0], time_span[1], 1000)
result = sol.sol(t_eval)
