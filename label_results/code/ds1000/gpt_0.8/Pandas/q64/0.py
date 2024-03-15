df['ID'] = df['name'].astype('category').cat.codes + 1
df = df.drop(columns=['name', 'a'])
df = df[['ID', 'b', 'c']]
