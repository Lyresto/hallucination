import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
import numpy as np
arr = np.zeros((20,10,10,2))



#print(arr)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(arr, file)
