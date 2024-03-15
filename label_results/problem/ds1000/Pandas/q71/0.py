result = df[df['c'] > 0.5][columns].sum(axis=1)
return pd.concat([df[df['c'] > 0.5], result.rename('sum')], axis=1)
### END SOLUTION
