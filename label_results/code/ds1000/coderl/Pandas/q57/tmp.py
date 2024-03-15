import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
import pandas as pd
from datetime import datetime




def datetime_to_seconds(dt):
    return int((dt - datetime(2022, 1, 1)).total_seconds())




def seconds_to_datetime(seconds):
    return datetime.strptime(f'{seconds:06d}', '%H:%M')



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)