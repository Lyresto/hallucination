import numpy as np

data = np.array([[4, 2, 5, 6, 7],
                 [5, 4, 3, 5, 7]])
bin_size = 3

num_bins = data.shape[1] // bin_size
binned_data = data[:, :num_bins*bin_size].reshape(data.shape[0], num_bins, bin_size)
bin_data_mean = np.mean(binned_data, axis=2)
END SOLUTION
