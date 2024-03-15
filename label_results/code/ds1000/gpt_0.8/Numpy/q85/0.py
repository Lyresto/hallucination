# Calculate the number of ones and zeros based on the given ratio
num_ones = int(one_ratio * size)
num_zeros = size - num_ones

# Create an array with the specified number of ones and zeros
ones = np.ones(num_ones)
zeros = np.zeros(num_zeros)

# Concatenate the arrays to get the final random array
nums = np.concatenate((ones, zeros))

# Shuffle the array to ensure randomness
np.random.shuffle(nums)
