def multiply_thru_frames(df1, df2):
	return (df1[["Timestamp", "data"]] * df2[["Timestamp", "data"]]).fillna(0)

def loop_through_each_row_of_df2(df1, df2, idx):
	df2_new = multiply_thru_frames(df2, df1)
	return df2_new[idx]
