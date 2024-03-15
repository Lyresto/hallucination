# Create a new column 'ID' by combining 'name' and 'a'
df['ID'] = df['name'] + df['a'].astype(str)

# Use pandas factorize function to convert 'ID' values to unique integer IDs
df['ID'] = pd.factorize(df['ID'])[0] + 1

# Drop the 'name' and 'a' columns
df = df.drop(['name', 'a'], axis=1)

result = df
