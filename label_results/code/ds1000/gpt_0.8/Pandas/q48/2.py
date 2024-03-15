# Identify rows whose value is greater than or equal to the threshold
high_val_rows = df.loc[df['value'] >= thresh]

# Calculate the average of the values of these rows
avg_val = high_val_rows['value'].mean()

# Replace the high value rows with a new row with the average value
new_row = pd.DataFrame({'lab': ['X'], 'value': [avg_val]})
new_row = new_row.set_index('lab')
df = df.loc[df['value'] < thresh].append(new_row)
