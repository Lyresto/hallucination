out = scipy.optimize.minimize(func, x0, args=(a,), bounds=zip(x_lower_bounds, x_true))
