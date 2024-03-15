# First, create a dictionary to map each unique combination of 'name' and 'a' to a unique ID
id_dict = {}
count = 1
for i, row in df.iterrows():
    name_a = (row['name'], row['a'])
    if name_a not in id_dict:
        id_dict[name_a] = count
        count += 1

# Then, use the dictionary to replace 'name' and 'a' with the corresponding ID
df['ID'] = df.apply(lambda row: id_dict[(row['name'], row['a'])], axis=1)
df = df[['ID', 'b', 'c']]
