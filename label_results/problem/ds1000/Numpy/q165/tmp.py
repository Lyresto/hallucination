import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
a = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
result = np.zeros((len(a), len(a))) # initialize result matrix with zeros
for i in range(len(a)):
    for j in range(len(a)):
        result[i][j] = np.linalg.norm(a[i]-a[j]) # calculate Euclidean distance between i-th and j-th point

#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
