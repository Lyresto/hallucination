out = scipy.optimize.minimize(func, x0, args=(a,), bounds=scipy.optimize.Bounds(x_lower_bounds, np.inf))
