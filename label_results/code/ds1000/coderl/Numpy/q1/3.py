from numpy import nan
x = np.array([1400, 1500, 1600, np.nan, np.nan, np.nan,1700])
x.remove(nan)
