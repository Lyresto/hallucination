result = df.sort_values(by=['keep_if_dup']).drop_duplicates(subset='url', keep='last')
