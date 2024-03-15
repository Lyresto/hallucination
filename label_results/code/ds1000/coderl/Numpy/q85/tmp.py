import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
size, one_ratio = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np




def rand_list(n, ratio):
    return np.random.randint(2, size=n)





def calculate_fraction(array):
    return 1 - array.sum() / float(array.size)



#print(nums)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(nums, file)
