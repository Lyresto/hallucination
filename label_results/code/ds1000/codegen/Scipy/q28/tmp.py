
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()

import numpy as np
from scipy import ndimage

def f(img):
    threshold = 0.75

    result = ndimage.gaussian_filter(img.astype(np.double), (30, 30))
    result -= result.min()
    result /= result.max()
    result = result.astype(np.int)
    result = result.sum(axis=0)
    result = result.sum(axis=1)
    result = result.sum(axis=2)
    result = result.sum(axis=3)
    result = result.sum(axis=4)
    result = result.sum(axis=5)
    result = result.sum(axis=6)
    result = result.sum(axis=7)
    result = result.sum(axis=8)
    result = result.sum(axis=9)
    result = result.sum(axis=10)
    result = result.sum(axis=11)
    result = result.sum(axis=12)
    result = result.sum(axis=13)
    result = result.sum(axis=14)
    result = result.sum(axis=15)
    result = result.sum(axis=16)
    result = result.sum(axis=17)
    result = result.sum(axis=18)
    result = result.sum(axis=19)
    result = result.sum(axis=20)
    result = result.sum(axis=21)
    result = result.sum(axis=22)
    result = result.sum(axis=23)
    result = result.sum(axis=24)
    result = result.sum(axis=25)
    result = result.sum(axis=26)
    result = result.sum(axis=27)
    result = result.sum(axis=28)
    result = result.sum(axis=29)
    result = result.sum(axis=30)
    result = result.sum(axis=31)
    result = result.sum(axis=32)
    result = result.sum(axis=33)
    result = result.sum(axis=34)
    result = result.sum(axis=35)
    result = result.sum(axis=36)
    result = result.sum(axis=37)
    result = result.sum(axis=38)
    result = result.sum(axis=39)
    result = result.sum(axis=40)
    result = result.sum(axis=41)
    result = result.sum(axis=42)
    result = result.sum(axis=43)
    result = result.sum(axis=44)
    result = result.sum(axis=45)
    result = result.sum(axis=46)
    result = result.sum(axis=47)

img = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
result = f(img)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
