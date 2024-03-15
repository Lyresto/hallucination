import dask.dataframe as dd
import pandas as pd

# Read the CSV file as a dask dataframe
df = dd.read_csv('file.csv')

# Split the 'var2' column using str.split and explode the resulting list
df = df.assign(var2=df['var2'].str.split(',')).explode('var2')

# Convert the dask dataframe to pandas dataframe
df = df.compute()

# Reset the index
df = df.reset_index(drop=True)

# Print the resulting dataframe
print(df)
