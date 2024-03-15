# Solution 1: using filter() to select columns containing 'val'
result = df.groupby('group').agg({"group_color": "first"})
result = result.join(df.filter(like='val').sum(axis=1).groupby(df['group']).sum(), rsuffix='_sum')
result.columns = ['group_color', 'val_sum']

# Solution 2: using iloc to select columns by index
result = df.groupby('group').agg({"group_color": "first"})
result = result.join(df.iloc[:, 2:].sum(axis=1).groupby(df['group']).sum(), rsuffix='_sum')
result.columns = ['group_color', 'val_sum']
