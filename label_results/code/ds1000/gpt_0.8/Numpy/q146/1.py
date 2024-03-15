min_vals = np.min(a, axis=1)
mask = np.equal(a, min_vals.reshape(-1, 1))
