result = pd.melt(df, value_vars=[tuple(col) for col in df.columns.values])
