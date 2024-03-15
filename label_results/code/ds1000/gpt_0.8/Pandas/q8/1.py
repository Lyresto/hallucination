result = df.drop_duplicates(subset='url', keep='first') | (df['drop_if_dup'] == 'No')
result = result.sort_values(by='id').reset_index(drop=True)
