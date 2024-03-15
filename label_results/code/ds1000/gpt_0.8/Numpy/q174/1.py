import numpy as np
import pandas as pd

lat=np.array([[10, 20, 30],
              [20, 11, 33],
              [21, 20, 10]])
lon=np.array([[100, 102, 103],
              [105, 101, 102],
              [100, 102, 103]])
val=np.array([[17, 2, 11],
              [86, 84, 1],
              [9, 5, 10]])

def f(lat, lon, val):
    # Flatten the arrays
    lat_flat = lat.flatten()
    lon_flat = lon.flatten()
    val_flat = val.flatten()
    
    # Create a dictionary with column names as keys and flattened arrays as values
    data = {'lat': lat_flat, 'lon': lon_flat, 'val': val_flat}
    
    # Create a DataFrame from the dictionary
    df = pd.DataFrame(data)
    
    return df

df = f(lat, lon, val)
print(df)