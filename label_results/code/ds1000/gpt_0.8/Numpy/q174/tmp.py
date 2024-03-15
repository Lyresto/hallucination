import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
import pandas as pd
lat, lon, val = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))



def f(lat, lon,val):
    import pandas as pd
    
    # Create a pandas DataFrame with columns 'lat', 'lon', 'val'
    df = pd.DataFrame({'lat': lat.flatten(), 'lon': lon.flatten(), 'val': val.flatten()})
    
    # Sort the DataFrame by the order of the original arrays
    df = df.sort_index()
    
    # Reset the index of the DataFrame
    df = df.reset_index(drop=True)
    
    # Return the resulting DataFrame
    return df


result = f(lat, lon, val)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
