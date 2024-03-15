b = np.eye(np.max(a)+1)[a.flatten()].reshape(a.shape + (np.max(a)+1,))
