result = np.where((x == a) & (y == b))[0][0] if np.any((x == a) & (y == b)) else -1
