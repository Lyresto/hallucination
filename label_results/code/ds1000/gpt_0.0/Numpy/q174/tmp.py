import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
import pandas as pd
lat, lon, val = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
def f(lat, lon,val):
    # Flatten the arrays and create a dictionary
    data_dict = {'lat': lat.flatten(), 'lon': lon.flatten(), 'val': val.flatten()}
    
    # Create the dataframe
    df = pd.DataFrame(data_dict)
    
    # Return the dataframe
    return df
    ### END SOLUTION
result = f(lat, lon, val)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
