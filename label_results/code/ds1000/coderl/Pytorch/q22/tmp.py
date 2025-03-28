import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import numpy as np
import pandas as pd
import torch

lens = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))



def get_mask(lens):
### BEGIN SOLUTION
    from itertools import chain
    
    


def get_mask(lens):
    x = [1] * len(lens)
    return list(chain.from_iterable([[0] * i for i in range(len(lens))]))



### END SOLUTION
mask = get_mask(lens)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(mask, f)
