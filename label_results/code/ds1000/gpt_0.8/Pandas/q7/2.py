result = df.drop_duplicates(subset='url', keep='first')
dup_idx = df[df.duplicated(subset='url', keep=False) & (df['keep_if_dup'] == 'Yes')].index
result = pd.concat([result, df.loc[dup_idx]], axis=0)
result = result.sort_index()
