import dask.dataframe as dd
import pandas as pd

# Read the CSV file into a Dask DataFrame
df = dd.read_csv('filename.csv')

# Split the 'var2' column into multiple rows
df = df.assign(var2=df.var2.str.split(','))

# Explode the 'var2' column into multiple rows
df = df.explode('var2')

# Convert back to pandas DataFrame
df = df.compute()

# Reset index
df = df.reset_index(drop=True)

result = df