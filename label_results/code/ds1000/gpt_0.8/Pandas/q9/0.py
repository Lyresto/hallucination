result = df.drop_duplicates(subset='url', keep='last').append(df[df['keep_if_dup']=='Yes'])
