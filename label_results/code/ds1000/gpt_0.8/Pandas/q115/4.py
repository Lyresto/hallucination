# Compute row totals
row_totals = df.sum(axis=1)

# Compute percentages
df.iloc[:, 1:] = df.iloc[:, 1:].div(row_totals, axis=0)

df