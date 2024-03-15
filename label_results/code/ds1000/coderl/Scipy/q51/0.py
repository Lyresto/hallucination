import scipy.stats
a = np.array([1., 2., 2.5, 4., 6.])
p, kurtosis = scipy.stats.kurtosis(a), scipy.stats.kurtosis(a, p=True)
print(kurtosis)
