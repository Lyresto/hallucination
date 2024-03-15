import numpy as np

def shift_array(arr, shifts):
    result = np.full_like(arr, np.nan)
    for i, shift in enumerate(shifts):
        if shift > 0:
            result[i, shift:] = arr[i, :-shift]
        elif shift < 0:
            result[i, :shift] = arr[i, -shift:]
        else:
            result[i] = arr[i]
    return result

a = np.array([[ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9.],
              [1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10.]])
shifts = [-2, 3]
result = shift_array(a, shifts)
result