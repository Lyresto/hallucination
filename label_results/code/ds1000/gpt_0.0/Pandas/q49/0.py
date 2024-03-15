# First, we create a mask to identify the rows that are not in the given section
mask = (df['value'] < section_left) | (df['value'] > section_right)

# Then, we calculate the average of the rows that will be substituted
avg = df.loc[~mask, 'value'].mean()

# We create a new row with the average value and a label to identify the substituted rows
new_row = pd.DataFrame({'lab':['X'], 'value':[avg]})

# Finally, we replace the rows that are not in the section with the new row
df.loc[~mask] = new_row.values

result = df
