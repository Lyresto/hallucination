def filt_series_df(df, filt):
	return df[df.index.get_level_values('a')!= filt.index.get_level_values('b') and
			  df.index.get_level_values('a').isin([x for x in filt.index.values if x!= df.index.get_level_values('b')]) and
			  df.index.get_level_values('b').isin([x for x in filt.index.values if x!= df.index.get_level_values('a')])]
