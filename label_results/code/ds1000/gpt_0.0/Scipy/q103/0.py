# Using scipy.signal.argrelextrema to find local minima and maxima
maxima_indices = signal.argrelextrema(arr, np.greater_equal, order=n)[0]
minima_indices = signal.argrelextrema(arr, np.less_equal, order=n)[0]

# Combining the indices and sorting them in ascending order
result = np.sort(np.concatenate((maxima_indices, minima_indices)))
