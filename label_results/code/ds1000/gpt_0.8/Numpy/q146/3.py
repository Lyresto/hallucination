mask = np.zeros_like(a, dtype=bool)
mask[np.arange(a.shape[0]), np.argmin(a, axis=1)] = True
