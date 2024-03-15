import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
data, bin_size = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
# First, reshape the data into a 3-dimensional array with shape (num_bins, bin_size, num_features)
num_bins = data.shape[1] // bin_size
data_3d = data[:, :num_bins*bin_size].reshape(data.shape[0], num_bins, bin_size)

# Calculate the mean along the second axis (the bin axis)
bin_data_mean = np.mean(data_3d, axis=1)

#print(bin_data_mean)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(bin_data_mean, file)
