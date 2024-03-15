# Solution 1: using filter() to select columns containing "val"
result = df.groupby('group').agg({"group_color": "first"})
result = result.join(df.filter(like="val").sum().add_prefix('total_'))

# Solution 2: using iloc() to select columns by index
value_cols = df.columns.get_loc("val1"): # get index of first value column
result = df.groupby('group').agg({"group_color": "first"})
result = result.join(df.iloc[:, value_cols:].sum().add_prefix('total_'))
