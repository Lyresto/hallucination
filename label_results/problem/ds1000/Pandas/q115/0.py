# Compute row totals
row_totals = df.iloc[:, 1:].sum(axis=1)

# Divide each value by its corresponding row total
df.iloc[:, 1:] = df.iloc[:, 1:].div(row_totals, axis=0)

# Round to 3 decimal places
df.iloc[:, 1:] = df.iloc[:, 1:].round(3)

# Rename columns
df.columns = ['cat', 'val1%', 'val2%', 'val3%', 'val4%']
