import numpy as np

def moving_window(arr, size):
    rows, cols = arr.shape
    padded_arr = np.pad(arr, ((1, 1), (1, 1)), mode='constant')
    result = []
    
    for i in range(rows):
        for j in range(cols):
            window = padded_arr[i:i+size[0], j:j+size[1]]
            result.append(window)
    
    return result

result = moving_window(a, size)
