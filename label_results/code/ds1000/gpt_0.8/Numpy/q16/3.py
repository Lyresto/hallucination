import numpy as np

def shift(arr, shifts):
    result = np.empty_like(arr)
    for i, shift in enumerate(shifts):
        if shift > 0:
            result[i] = np.concatenate((np.full(shift, np.nan), arr[i, :-shift]))
        elif shift < 0:
            result[i] = np.concatenate((arr[i, -shift:], np.full(-shift, np.nan)))
        else:
            result[i] = arr[i]
    return result
