df.index.set_levels(pd.to_datetime(df.index.levels[1]), level=1, inplace=True)
