# identify rows to aggregate
to_agg = df.loc[df['value'] >= thresh]
# calculate average of these rows
avg = to_agg.mean()
# create new row with index 'X' and value 'avg'
new_row = pd.DataFrame({'lab':['X'], 'value':[avg[0]]})
new_row = new_row.set_index('lab')
# remove rows to aggregate from original dataframe
df = df.loc[df['value'] < thresh]
# concatenate new row and original dataframe
result = pd.concat([df, new_row])
