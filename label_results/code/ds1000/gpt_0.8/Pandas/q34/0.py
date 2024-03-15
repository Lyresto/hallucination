# Solution 1: using filter() to select columns with 'val' in their name
result = df.groupby('group').agg({"group_color": "first"})
result = result.join(df.filter(like='val').sum(axis=1).rename('val_sum'))
