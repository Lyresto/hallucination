df_shuffled = df.iloc[List].reset_index(drop=True)
result = len(df_shuffled[df_shuffled['Type'] != df['Type']])
