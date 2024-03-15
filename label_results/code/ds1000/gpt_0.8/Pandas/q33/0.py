# Get all column names that contain 'val'
val_cols = [col for col in df.columns if 'val' in col]

# Get a dictionary with the mean aggregation for each value column
agg_dict = {col: 'mean' for col in val_cols}

# Add 'group_color' to the dictionary to make sure it stays in the result
agg_dict['group_color'] = 'first'

# Group by 'group' and aggregate using the agg_dict
result = df.groupby('group').agg(agg_dict)
