result = np.maximum.reduceat(a, np.where(np.diff(index) != 0)[0] + 1)
