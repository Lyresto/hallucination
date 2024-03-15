import numpy as np
a = np.array([[[1, 1, 1],
               [1, 1, 1],
               [1, 1, 1]],
              
              [[3, 3, 3],
               [3, 2, 3],
               [3, 3, 3]],
              
              [[2, 2, 2],
               [2, 3, 2],
               [2, 2, 2]]])

b = np.array([[[0, 1, 2],
               [3, 4, 5],
               [6, 7, 8]],
              
              [[9, 10, 11],
               [12, 13, 14],
               [15, 16, 17]],
              
              [[18, 19, 20],
               [21, 22, 23],
               [24, 25, 26]]])

# Calculate the sum along the last axis of a
sum_a = np.sum(a, axis=-1)

# Get the indices that would sort the sum_a array
sort_indices = np.argsort(sum_a)

# Use the sort indices to sort the b array
sorted_b = b[sort_indices]

sorted_b