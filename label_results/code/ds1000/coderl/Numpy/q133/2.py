def time_stamp_to_array(df, cat_col, cat_major_col, index):
	return [[df[cat_col].values.tolist(), df[cat_major_col].values.tolist(), index.values.tolist()]]
