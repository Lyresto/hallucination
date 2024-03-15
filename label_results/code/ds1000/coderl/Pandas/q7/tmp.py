import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 18:46:52 2019

@author: Greg
"""
import collections




def drop_duplicates(df, keep_first=False):
    # Your code goes here
    output = []
    for key in df.keys():
        value = df[key]
        if keep_first and value.duplicated():
            continue
        output.append([key, value.value, value.duplicated()])

    return output



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)