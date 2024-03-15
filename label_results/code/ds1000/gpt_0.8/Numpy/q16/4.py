import numpy as np

def shift(arr, shift_values):
    shifted_arr = np.empty_like(arr)
    for i, shift in enumerate(shift_values):
        shifted_arr[i] = np.roll(arr[i], shift)
    return shifted_arr

shifted_arr = shift(a, shift)
shifted_arr