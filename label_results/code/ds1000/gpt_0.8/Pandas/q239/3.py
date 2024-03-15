result = pd.concat([df1, df2], axis=0)
result = result.sort_values(['id', 'date']).fillna(method='ffill')
