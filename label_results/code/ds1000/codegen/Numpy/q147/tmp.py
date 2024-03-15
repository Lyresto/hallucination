import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
post, distance = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
post = [2, 5, 6, 10]
distance = [50, 100, 500, 1000]
result = np.corrcoef(post, distance)

#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
