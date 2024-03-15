
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()

import numpy as np
from scipy import ndimage




def f(img):
    threshold = 0.75
from math import ceil



def f(img = example_img):
    return ceil(sum(sum(img[i*512:(i+1)*512, j*512:(j+1)*512] > threshold * threshold for i in range(504)) / 4)



img = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
result = f(img)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
