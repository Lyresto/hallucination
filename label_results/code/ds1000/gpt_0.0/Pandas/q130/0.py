df['index_original'] = df.index
duplicate_bool = df.duplicated(subset=['col1','col2'], keep='first')
result = df.loc[duplicate_bool == True]
result = result.merge(df[['col1','col2','index_original']], on=['col1','col2'], how='left')
result = result[['col1','col2','index_original']]
