import numpy as np

def shift(arr, shifts):
    result = np.empty_like(arr)
    for i in range(arr.shape[0]):
        result[i] = np.roll(arr[i], shifts[i])
    return result

a = np.array([[ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9.],
              [1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10.]])
shifts = [-2, 3]
result = shift(a, shifts)
result