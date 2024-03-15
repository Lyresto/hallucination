def objective(x):
    return np.sum(a.dot(x ** 2))

out = scipy.optimize.minimize(objective, x0, method='L-BFGS-B', bounds=[(lb, None) for lb in x_lower_bounds])
