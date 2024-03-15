def objective(x, a, y):
    return np.sum(a * x**2 - y)**2

out = scipy.optimize.minimize(objective, x0, args=(a, y), method='L-BFGS-B', bounds=[(lb, None) for lb in x_lower_bounds])
