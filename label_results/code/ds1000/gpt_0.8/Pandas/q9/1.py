result = df.sort_values('keep_if_dup', ascending=False).drop_duplicates(subset='url', keep='last').sort_index()
