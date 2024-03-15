result = df.drop_duplicates(subset='url', keep='first')
result = pd.concat([result, df[df['keep_if_dup']=='Yes']])
