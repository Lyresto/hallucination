# First, we select the rows with value >= threshold and calculate their mean
mask = df['value'] >= thresh
avg_value = df.loc[mask, 'value'].mean()

# Then, we select the rows with value < threshold
df_below_thresh = df.loc[~mask]

# We create a new row with the average value and a new label
new_row = pd.DataFrame({'value': [avg_value]}, index=['X'])

# Finally, we concatenate the two dataframes and sort by index
result = pd.concat([df_below_thresh, new_row]).sort_index()
