result = np.maximum.reduceat(a, np.arange(len(a))[index[:-1] != index[1:]])
