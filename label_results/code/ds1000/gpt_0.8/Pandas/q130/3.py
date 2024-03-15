df['index_original'] = df.groupby(['col1', 'col2']).transform('first')
duplicate = df[df.duplicated(subset=['col1', 'col2'], keep='first')]
result = duplicate[['col1', 'col2', 'index_original']]
