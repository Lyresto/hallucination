
    result = np.zeros((a.shape[0], b.shape[0]))
    for i in range(a.shape[0]):
        for j in range(b.shape[0]):
            result[i, j] = np.mean(a[i, :] + b[j, :])
    ### END SOLUTION
    return result
