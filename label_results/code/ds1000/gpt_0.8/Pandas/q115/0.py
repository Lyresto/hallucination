df['total'] = df.sum(axis=1)
df.loc[:, 'val1':'val4'] = df.loc[:, 'val1':'val4'].div(df['total'], axis=0)
df = df.drop(columns='total')
df