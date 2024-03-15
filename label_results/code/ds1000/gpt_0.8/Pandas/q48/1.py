# First, filter out the rows above the threshold
df_below_thresh = df.loc[df['value'] < thresh]

# Then, calculate the average of the remaining rows
df_above_thresh = df.loc[df['value'] >= thresh]
avg = df_above_thresh['value'].mean()

# Combine the two dataframes
new_df = pd.concat([df_below_thresh, pd.DataFrame({'value': [avg]}, index=['X'])])

# Sort the index
result = new_df.sort_index()
