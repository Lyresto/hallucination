# Create a mask for values less than n1
mask1 = arr < n1[:, np.newaxis]

# Create a mask for values greater or equal to n2
mask2 = arr >= n2[:, np.newaxis]

# Set values less than n1 to 0
arr[mask1] = 0

# Add 5 to values that are neither less than n1 nor greater or equal to n2
arr[~(mask1 | mask2)] += 5

# Set values greater or equal to n2 to 30
arr[mask2] = 30

# END SOLUTION
