result = df.groupby('username')['views'].apply(lambda x: pd.cut(x, bins).value_counts()).unstack(fill_value=0)
