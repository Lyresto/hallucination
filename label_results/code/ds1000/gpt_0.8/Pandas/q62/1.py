# Solution 1: using Pandas' factorize method

df['a'], _ = pd.factorize(df['a'])

# Solution 2: using a dictionary and map method

unique_vals = df['a'].unique()
id_dict = {val: i+1 for i, val in enumerate(unique_vals)}
df['a'] = df['a'].map(id_dict)

# Note: both solutions assume that the IDs should start at 1 and increase sequentially

result = df
