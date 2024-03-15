df['transaction'] = df[['time', 'amount']].apply(tuple, axis=1)
result = df.groupby('user')['transaction'].apply(list)
