import numpy as np

data = np.array([[4, 2, 5, 6, 7],
                 [5, 4, 3, 5, 7]])
bin_size = 3

num_bins = data.shape[1] // bin_size
bin_data = np.array_split(data, num_bins, axis=1)

bin_data_mean = [np.mean(bin, axis=1) for bin in bin_data]

bin_data_mean