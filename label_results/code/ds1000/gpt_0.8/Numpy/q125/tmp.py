import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
data, bin_size = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np

data = np.array([[4, 2, 5, 6, 7],
                 [5, 4, 3, 5, 7]])

bin_size = 3

num_bins = data.shape[1] // bin_size

# Reshape the data array into bins
binned_data = data[:, :num_bins * bin_size].reshape(data.shape[0], num_bins, bin_size)

# Calculate the mean of each bin
bin_data_mean = np.mean(binned_data, axis=2)

bin_data_mean


#print(bin_data_mean)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(bin_data_mean, file)
