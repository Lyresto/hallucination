result = df.groupby('user').apply(lambda x: x[['time', 'amount']].values.tolist()).rename('transactions')
