def sort_df(df):
	sorted_df = df.sort_values(by=['treatment', 'dose', 'time'], ascending=False)
	return sorted_df
