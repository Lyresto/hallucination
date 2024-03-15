A = [float(x) if x != 'np.inf' else np.inf for x in A]
AVG = np.mean(A)
