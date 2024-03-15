# Calculate the number of 1's and 0's based on the desired ratio and size
num_ones = int(size * one_ratio)
num_zeros = size - num_ones

# Create an array with the desired number of 1's and 0's
ones_array = np.ones(num_ones, dtype=int)
zeros_array = np.zeros(num_zeros, dtype=int)

# Concatenate the arrays to get the final random array with the desired ratio
nums = np.concatenate((ones_array, zeros_array))

# Shuffle the array to make it random
np.random.shuffle(nums)
