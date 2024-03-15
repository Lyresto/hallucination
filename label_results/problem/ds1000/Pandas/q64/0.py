df['ID'] = df.groupby(['name', 'a']).ngroup() + 1
result = df[['ID', 'b', 'c']]
