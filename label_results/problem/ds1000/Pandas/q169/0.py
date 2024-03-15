df = df.loc[:, (df != 0).any(axis=0)]
df = df.loc[(df != 0).any(axis=1)]
result = df
