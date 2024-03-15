df['index'] = df.index
df['Random'] = df.groupby('UserId')['index'].transform(lambda x: x.sample(frac=0.2, random_state=0))
df.loc[df['Random'].notnull(), 'Quantity'] = 0
df = df.drop(['index', 'Random'], axis=1)
