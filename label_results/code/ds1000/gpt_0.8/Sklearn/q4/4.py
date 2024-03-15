# Step 1: Split the list into separate elements
df['Col3'] = df['Col3'].apply(lambda x: x.split(','))

# Step 2: Create a set of unique elements
unique_elements = set()
for lst in df['Col3']:
    unique_elements.update(lst)

# Step 3: Create new columns for each unique element
for element in unique_elements:
    df[element] = df['Col3'].apply(lambda x: 1 if element in x else 0)

# Step 4: Drop the original column
df.drop('Col3', axis=1, inplace=True)

df_out = df
