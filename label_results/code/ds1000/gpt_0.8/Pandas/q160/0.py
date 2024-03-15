df_sorted = df.groupby('cokey').apply(lambda x: x.sort_values('A'))
result = df_sorted.reset_index(drop=True)
