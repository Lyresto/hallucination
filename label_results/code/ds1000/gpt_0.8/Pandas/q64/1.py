# Create a dictionary to map unique ID to each name-a combination
id_dict = {}
current_id = 1
for index, row in df.iterrows():
    name_a = row['name'] + str(row['a'])
    if name_a not in id_dict:
        id_dict[name_a] = current_id
        current_id += 1

# Create a new column 'ID' using the mapping dictionary
df['ID'] = df.apply(lambda row: id_dict[row['name'] + str(row['a'])], axis=1)

# Drop the 'name' and 'a' columns
df = df.drop(['name', 'a'], axis=1)

# Reorder columns
df = df[['ID', 'b', 'c']]
