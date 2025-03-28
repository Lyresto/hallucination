# One way to dynamically take the sum of all columns containing "val" in their names is to use
# a list comprehension to filter the columns and then use the sum() method

value_cols = [col for col in df.columns if 'val' in col]
result = df.groupby('group').agg({"group_color": "first", **{col: "sum" for col in value_cols}})
