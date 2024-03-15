import dask.dataframe as dd

# Read the CSV file into a Dask DataFrame
df = dd.read_csv('file.csv')

# Split the 'var2' column into multiple rows
df = df.assign(var2=df['var2'].str.split(','))

# Explode the 'var2' column into multiple rows
df = df.explode('var2')

# Reset the index
df = df.reset_index(drop=True)

# Display the resulting Dask DataFrame
df.compute()
