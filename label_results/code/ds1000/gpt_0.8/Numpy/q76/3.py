result = np.empty_like(array_of_arrays)
for i in range(array_of_arrays.shape[0]):
    result[i] = np.copy(array_of_arrays[i])
