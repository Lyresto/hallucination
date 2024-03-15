result = pd.melt(df, value_vars=[(a, b, c) for a, b, c in zip(df.columns.get_level_values(0), df.columns.get_level_values(1), df.columns.get_level_values(2))])
