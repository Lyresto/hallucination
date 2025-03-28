import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
data, bin_size = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np



def mean(arr, size):
    return np.mean(np.array(arr).reshape(-1, size)).tolist()



#print(bin_data_mean)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(bin_data_mean, file)
