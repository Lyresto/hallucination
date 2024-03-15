import numpy as np
arr = (np.random.rand(5, 50)-0.5) * 50
n1 = [1,2,3,4,5]
n2 = [6,7,8,9,10]

arr_temp = arr.copy()
mask = arr_temp < np.array(n1)[:, np.newaxis]
mask2 = arr_temp >= np.array(n2)[:, np.newaxis]
mask3 = np.logical_xor(mask, mask2)
arr[mask] = 0
arr[mask3] = arr_temp[mask3] + 5
arr[~mask2] = 30 

print(arr)