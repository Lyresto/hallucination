result = df.drop_duplicates(subset='url', keep=lambda x: 'Yes' not in df.loc[x]['keep_if_dup'].tolist())
