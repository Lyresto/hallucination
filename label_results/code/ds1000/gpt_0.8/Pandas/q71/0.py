result = df[df.c > 0.5][columns].sum(axis=1)
df.loc[df.c > 0.5, 'sum'] = result
return df[df.c > 0.5][['a', 'd', 'sum']]
### END SOLUTION
