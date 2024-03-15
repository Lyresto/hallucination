# Get the list of all columns that contain 'val'
val_cols = [col for col in df.columns if 'val' in col]

# Create a dictionary of aggregation functions for each value column
agg_dict = {}
for col in val_cols:
    agg_dict[col] = 'mean'

# Group by 'group' and apply the aggregation dictionary
result = df.groupby('group').agg({"group_color": "first", **agg_dict})
