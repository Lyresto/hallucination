num_ones = int(size * one_ratio)
num_zeros = size - num_ones
ones = np.ones(num_ones, dtype=int)
zeros = np.zeros(num_zeros, dtype=int)
nums = np.concatenate((ones, zeros))
np.random.shuffle(nums)
