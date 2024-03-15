# create a dictionary to map unique IDs to each name
name_dict = {}
count = 1
for name in df['name'].unique():
    name_dict[name] = count
    count += 1

# use the map method to replace the 'a' column with the unique IDs
df['a'] = df['name'].map(name_dict)

result = df
