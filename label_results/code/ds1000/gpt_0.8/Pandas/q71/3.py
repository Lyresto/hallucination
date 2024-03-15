result = df.loc[df['c']>0.5, columns].apply(sum, axis=1).reset_index(name='sum')
return pd.concat([df.loc[df['c']>0.5], result['sum']], axis=1)
### END SOLUTION
