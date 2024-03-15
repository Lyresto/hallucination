stdMeann = lambda x: pd.Series({'mean': x.mean(), 'std': x.std()})
result = df.groupby('b').a.apply(stdMeann).reset_index()
result = result.set_index('b')
