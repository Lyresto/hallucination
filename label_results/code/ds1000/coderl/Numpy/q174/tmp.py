import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
import pandas as pd
lat, lon, val = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))



def f(lat, lon,val):
    from numpy import concatenate
    
    


def f(lat=example_lat, lon=example_lon, val=example_val):
    lat_values = concatenate((lat, lat), axis=0)
    lon_values = concatenate((lon, lon), axis=0)
    val_values = concatenate((val, val), axis=0)
    return pd.DataFrame({'lat': lat_values, 'lon': lon_values, 'val': val_values})



result = f(lat, lon, val)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
