# First, replace all 0 values with NaN
df.replace(0, pd.np.nan, inplace=True)

# Then, calculate the cumulative sum for each row from end to head
cumulative_sum = df.iloc[:, 1:].iloc[:, ::-1].cumsum(axis=1).iloc[:, ::-1]

# Calculate the number of non-zero values for each row
non_zero_count = df.iloc[:, 1:].apply(lambda x: x[x.notnull()].count(), axis=1)

# Calculate the cumulative average for each row from end to head
cumulative_avg = cumulative_sum.div(non_zero_count, axis=0)

# Replace NaN values with 0
cumulative_avg.fillna(0, inplace=True)

# Combine the Name column with the cumulative average dataframe
df = pd.concat([df['Name'], cumulative_avg], axis=1)
