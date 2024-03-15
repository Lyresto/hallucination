import numpy as np

arr = (np.random.rand(5, 50)-0.5) * 50
n1 = [1,2,3,4,5]
n2 = [6,7,8,9,10]

# Create a boolean mask for values in arr that are lower than n1
mask1 = arr < np.array(n1)[:, None]

# Create a boolean mask for values in arr that are greater or equal to n2
mask2 = arr >= np.array(n2)[:, None]

# Set values in arr that are lower than n1 to 0
arr[mask1] = 0

# Add 5 to values in arr that are not lower than n1 and not greater or equal to n2
arr[~mask1 & ~mask2] += 5

# Set values in arr that are greater or equal to n2 to 30
arr[mask2] = 30

END SOLUTION

print(arr)