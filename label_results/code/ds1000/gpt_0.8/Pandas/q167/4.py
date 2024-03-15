result = df.groupby('b')['a'].agg(['mean', 'std'])
result