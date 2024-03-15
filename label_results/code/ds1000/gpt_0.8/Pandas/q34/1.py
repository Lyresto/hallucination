# Solution 1: Using filter() method to get all columns containing 'val'
result = df.groupby('group').agg({'group_color': 'first'})
result = result.join(df.filter(like='val').sum(axis=1).rename('total_value'))

# Solution 2: Using iloc to slice the value columns and sum them up
result = df.groupby('group').agg({'group_color': 'first'})
result = result.join(df.iloc[:, 2:].sum(axis=1).rename('total_value'))

# Solution 3: Using loc to slice the value columns and sum them up
result = df.groupby('group').agg({'group_color': 'first'})
result = result.join(df.loc[:, 'val1':].sum(axis=1).rename('total_value'))
