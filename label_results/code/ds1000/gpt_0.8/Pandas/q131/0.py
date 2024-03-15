df['index_original'] = df.duplicated(subset=['col1','col2'], keep='last').map({True: df[df.duplicated(subset=['col1','col2'], keep='last')].index[0]})
