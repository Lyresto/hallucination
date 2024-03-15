result = pd.concat([df1, df2], axis=0)
result = result.sort_values(by=['id', 'date'])
result['city'] = result['city'].fillna(method='ffill')
result['district'] = result['district'].fillna(method='ffill')
result = result.reset_index(drop=True)
result
