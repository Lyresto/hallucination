result = df.groupby('l')['v'].apply(lambda x: np.nan if x.isnull().any() else x.sum())
