col_array = a[:, col] * multiply_number
cumulative_sum = np.cumsum(col_array)
result = cumulative_sum
