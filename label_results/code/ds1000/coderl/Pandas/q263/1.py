def filter_df_by_other(df, filt):
	return df[df.index.get_level_values('a').isin(filt.index.get_level_values('a')) &
		   df.index.get_level_values('b').isin(filt.index.get_level_values('b'))]
