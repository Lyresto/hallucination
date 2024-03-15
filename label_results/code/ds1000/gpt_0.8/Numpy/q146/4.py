# Find the minimum value along axis 1
min_values = np.min(a, axis=1)

# Create a mask array with True where the value is equal to the minimum value along axis 1, False otherwise
mask = a == min_values[:, np.newaxis]
END SOLUTION
