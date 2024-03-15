df['ID'] = (df['name'] + df['a'].astype(str)).astype('category').cat.codes + 1
result = df[['ID', 'b', 'c']]
