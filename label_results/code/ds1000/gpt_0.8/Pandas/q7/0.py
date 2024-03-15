result = df.drop_duplicates(subset='url', keep='first')
duplicates = df[df.duplicated(subset='url', keep=False)]
result = pd.concat([result, duplicates[duplicates['keep_if_dup'] == 'Yes']])
