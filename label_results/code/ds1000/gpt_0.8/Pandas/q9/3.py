result = df.groupby('url').apply(lambda x: x if 'Yes' in x['keep_if_dup'].values else x.tail(1)).reset_index(drop=True)
