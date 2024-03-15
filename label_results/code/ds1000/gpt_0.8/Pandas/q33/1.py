# Using filter to get all columns containing "val" in their names
val_cols = df.filter(like='val').columns

# Using groupby and mean functions on the filtered columns
result = df.groupby('group').agg({"group_color": "first", **{col: "mean" for col in val_cols}})
