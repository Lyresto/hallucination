out = scipy.optimize.minimize(func, x0, args=(a,), method='L-BFGS-B', bounds=[(lb, None) for lb in x_lower_bounds])
