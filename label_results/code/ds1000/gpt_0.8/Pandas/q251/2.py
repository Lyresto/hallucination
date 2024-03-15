df_expanded = df['codes'].apply(pd.Series)
result = pd.concat([df, df_expanded], axis=1).drop('codes', axis=1)
