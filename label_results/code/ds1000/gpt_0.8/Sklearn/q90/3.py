import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

df1 = load_data() # load the dataframe

slopes = [] # create an empty list to store the slopes

for col in df1.columns[1:]: # iterate over all columns except the first one ('Time')
    df2 = df1[~np.isnan(df1[col])] # remove rows with NaN values in the current column
    df3 = df2[['Time', col]] # select only the 'Time' and current column
    npMatrix = np.matrix(df3) # convert to numpy matrix
    X, Y = npMatrix[:,0], npMatrix[:,1] # separate X and Y variables
    slope = LinearRegression().fit(X,Y) # perform linear regression
    m = slope.coef_[0] # extract the slope coefficient
    slopes.append(m) # append the slope to the list

slopes = np.array(slopes) # convert the list to a numpy array
END SOLUTION