result = np.array([a[i:i+2, j:j+2] for i in range(0, a.shape[0], 2) for j in range(0, a.shape[1], 2)])
