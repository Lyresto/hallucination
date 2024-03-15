# Compute the row sums
row_sums = df.iloc[:, 1:].sum(axis=1)

# Divide each value by the row sum and multiply by 100 to get the percentage
df.iloc[:, 1:] = (df.iloc[:, 1:] / row_sums[:, None]) * 100

df