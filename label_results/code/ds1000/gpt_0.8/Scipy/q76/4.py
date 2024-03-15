def objective(x):
    return np.sum(a.dot(x ** 2))

out = scipy.optimize.minimize(objective, x0, bounds=scipy.optimize.Bounds(x_lower_bounds, np.inf))
