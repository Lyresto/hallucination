# Get all columns starting with 'Value'
value_cols = [col for col in df.columns if col.startswith('Value')]

# Filter rows where absolute value of all 'Value' columns is less than 1
df = df[(df[value_cols].abs() < 1).all(axis=1)]
