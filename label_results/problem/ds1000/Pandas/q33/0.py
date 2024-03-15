# Get all columns that contain "val" in their name
val_cols = [col for col in df.columns if "val" in col]

# Group by "group" column and take the mean of all value columns
result = df.groupby("group")[val_cols].mean().reset_index()

# Add the first value of "group_color" column to the result
result["group_color"] = df.groupby("group")["group_color"].first().values
