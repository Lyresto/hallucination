result = df.drop_duplicates(subset='url', keep=lambda x: x.keep_if_dup.iloc[0] == 'No')
