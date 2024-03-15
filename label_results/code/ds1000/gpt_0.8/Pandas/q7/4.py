result = df.drop_duplicates(subset='url', keep='first')
for index, row in df.iterrows():
    if row['keep_if_dup'] == 'Yes':
        result = result.append(row)
