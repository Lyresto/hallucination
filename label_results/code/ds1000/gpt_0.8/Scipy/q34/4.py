mean = col.mean()
standard_deviation = np.sqrt(col.power(2).mean() - mean**2)
