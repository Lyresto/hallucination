import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

df1 = load_data()  # Load the dataframe

slopes = []  # Initialize an empty list to store the slopes

for col in df1.columns:  # Iterate over each column in the dataframe
    if col != 'Time':  # Exclude the 'Time' column
        df2 = df1[~np.isnan(df1[col])]  # Filter out rows with NaN values in the current column
        df3 = df2[['Time', col]]  # Select only the 'Time' and current column
        npMatrix = np.matrix(df3)  # Convert the filtered dataframe to numpy matrix
        X, Y = npMatrix[:, 0], npMatrix[:, 1]  # Separate the 'Time' and current column as X and Y
        slope = LinearRegression().fit(X, Y)  # Fit a linear regression model
        m = slope.coef_[0]  # Get the slope coefficient
        slopes.append(m)  # Append the slope coefficient to the list

END SOLUTION