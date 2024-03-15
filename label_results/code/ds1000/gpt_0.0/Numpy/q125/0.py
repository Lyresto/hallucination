# First, reshape the data into a 3-dimensional array with shape (num_bins, bin_size, num_features)
num_bins = data.shape[1] // bin_size
data_3d = data[:, :num_bins*bin_size].reshape(data.shape[0], num_bins, bin_size)

# Calculate the mean along the second axis (the bin axis)
bin_data_mean = np.mean(data_3d, axis=1)
