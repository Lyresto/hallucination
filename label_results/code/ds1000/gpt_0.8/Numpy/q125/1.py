import numpy as np

data = np.array([[4, 2, 5, 6, 7],
                 [5, 4, 3, 5, 7]])
bin_size = 3

bin_data = [data[:, i:i+bin_size] for i in range(0, data.shape[1], bin_size)]
bin_data_mean = [np.mean(bin, axis=1) for bin in bin_data]
bin_data_mean = np.array(bin_data_mean)

bin_data_mean