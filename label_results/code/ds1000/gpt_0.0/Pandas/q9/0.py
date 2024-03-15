result = df.drop_duplicates(subset='url', keep='last')
result = result.groupby('url').apply(lambda x: x if 'Yes' in x['keep_if_dup'].values else x.drop_duplicates(subset='keep_if_dup', keep='last'))
result = result.reset_index(drop=True)
