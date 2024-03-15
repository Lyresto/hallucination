df_shuffled = df.iloc[List].reset_index(drop=True)
different_types = sum(df_shuffled['Type'] != df['Type'])
result = different_types
