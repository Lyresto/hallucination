result = df.drop_duplicates(subset='url', keep='first').append(df[df['drop_if_dup'] == 'No'])
