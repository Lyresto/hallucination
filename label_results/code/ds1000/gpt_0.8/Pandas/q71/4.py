result = df.loc[df['c'] > 0.5, columns]
result['sum'] = result.sum(axis=1)
return result
### END SOLUTION
