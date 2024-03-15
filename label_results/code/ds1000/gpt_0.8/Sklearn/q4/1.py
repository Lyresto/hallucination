# Step 1: Create a set of unique elements
unique_elements = set()
for row in df['Col3']:
    unique_elements.update(row)

# Step 2: Create a dictionary to store the one-hot encoded values
one_hot_dict = {}
for element in unique_elements:
    one_hot_dict[element] = []

# Step 3: Iterate over each row and update the dictionary with the one-hot encoded values
for row in df.iterrows():
    row_values = row[1]
    for element in unique_elements:
        if element in row_values['Col3']:
            one_hot_dict[element].append(1)
        else:
            one_hot_dict[element].append(0)

# Step 4: Create a new dataframe using the one-hot encoded values
df_out = pd.DataFrame(one_hot_dict)

# Step 5: Concatenate the original dataframe and the new one-hot encoded dataframe
df_out = pd.concat([df, df_out], axis=1)

# Step 6: Drop the original column with the list of elements
df_out = df_out.drop('Col3', axis=1)
