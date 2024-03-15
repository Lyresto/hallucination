df['total'] = df.sum(axis=1)
df.iloc[:, 1:] = df.iloc[:, 1:].div(df['total'], axis=0)
df.drop(columns='total', inplace=True)
df