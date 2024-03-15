# Using list comprehension to add 'X' to all column headers
new_columns = [col+'X' if not col.endswith('X') else col for col in df.columns]

# Renaming all columns with new column headers
df.columns = new_columns
