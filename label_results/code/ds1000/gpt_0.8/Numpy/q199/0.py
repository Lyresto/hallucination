import numpy as np
arr = (np.random.rand(5, 50)-0.5) * 50
n1 = [1,2,3,4,5]
n2 = [6,7,8,9,10]

mask1 = arr < np.array(n1)[:, np.newaxis]
mask2 = arr >= np.array(n2)[:, np.newaxis]
mask3 = mask1 ^ mask2

arr[mask1] = 0
arr[mask2] = 30
arr[mask3] += 5

END SOLUTION