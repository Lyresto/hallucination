import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
a, number = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
is_contained = number in a

#print(is_contained)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(is_contained, file)
