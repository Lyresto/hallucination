arr_temp = arr.copy()
for i in range(arr.shape[0]):
    mask1 = arr_temp[i] < n1[i]
    mask2 = arr_temp[i] >= n2[i]
    mask3 = ~(mask1 | mask2)
    arr[i][mask1] = 0
    arr[i][mask2] = 30
    arr[i][mask3] += 5
