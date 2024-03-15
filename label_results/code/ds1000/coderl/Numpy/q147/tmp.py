import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
post, distance = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np



def correlation(post, distance):
    post = np.array(post)
    distance = np.array(distance)
    return np.sum(np.array(post).reshape(-1, 1) * np.array(distance).reshape(-1, 1)) / (np.array(post).sum() - np.array(distance).sum())



#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
