df['row_total'] = df.sum(axis=1)
df.iloc[:, 1:] = df.iloc[:, 1:].div(df['row_total'], axis=0)
df = df.drop(columns='row_total')
df