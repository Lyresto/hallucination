df.groupby('l')['v'].apply(lambda x: x.sum(skipna=False))