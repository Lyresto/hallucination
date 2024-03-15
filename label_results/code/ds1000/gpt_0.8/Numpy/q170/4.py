A = ['np.inf', '33.33', '33.33', '33.37']
NA = np.asarray([float(x) if x != 'np.inf' else np.inf for x in A])
AVG = np.mean(NA, axis=0)
