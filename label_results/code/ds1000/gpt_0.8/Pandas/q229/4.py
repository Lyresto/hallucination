result = df.groupby('username')['views'].apply(lambda x: pd.cut(x, bins).value_counts()).unstack().fillna(0).astype(int)
