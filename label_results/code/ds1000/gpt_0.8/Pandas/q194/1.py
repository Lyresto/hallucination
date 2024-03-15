import dask.dataframe as dd
import pandas as pd

df = pd.DataFrame([["A", "Z,Y"], ["B", "X"], ["C", "W,U,V"]], index=[1,2,3], columns=['var1', 'var2'])

# Convert pandas dataframe to dask dataframe
ddf = dd.from_pandas(df, npartitions=1)

# Split the var2 column using a comma as the delimiter
ddf['var2'] = ddf['var2'].str.split(',')

# Explode the var2 column to create multiple rows
ddf = ddf.explode('var2')

# Convert dask dataframe back to pandas dataframe
result = ddf.compute()

result