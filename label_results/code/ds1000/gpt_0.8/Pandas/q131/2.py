df['index_original'] = df.duplicated(subset=['col1','col2'], keep='last')
df['index_original'] = df['index_original'].apply(lambda x: df[df.duplicated(subset=['col1','col2'], keep='last')].index[0] if x else None)
