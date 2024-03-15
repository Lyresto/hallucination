sums = np.sum(a, axis=(1,2))
sorted_indices = np.argsort(sums)
result = b[sorted_indices]
