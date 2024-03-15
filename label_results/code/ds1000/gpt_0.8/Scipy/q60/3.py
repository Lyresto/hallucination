new_array = np.zeros((len(x_new), array.shape[1], array.shape[2]))
for i in range(array.shape[1]):
    for j in range(array.shape[2]):
        f = scipy.interpolate.interp1d(x, array[:, i, j])
        new_array[:, i, j] = f(x_new)
