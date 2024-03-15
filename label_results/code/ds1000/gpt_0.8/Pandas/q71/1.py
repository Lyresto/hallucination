result = df[df.c > 0.5][columns].sum(axis=1)
result.name = 'sum'
return pd.concat([df[df.c > 0.5], result], axis=1)
### END SOLUTION