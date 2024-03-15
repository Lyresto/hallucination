import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import torch
import numpy as np
a = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import torch




def convert_array_to_tensor(a):
    a_pt = []
    for x in a:
        a_pt.append(torch.from_numpy(x))
    return a_pt



#print(a_pt)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(a_pt, file)
