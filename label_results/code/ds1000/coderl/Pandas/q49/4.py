from statistics import mean
def section_average(df, section_left, section_right):
	sub_df = df.copy()
	for i in range(section_left, section_right):
		sub_df[i] = mean(sub_df[i])
	return sub_df.loc[df['value'].isin(list(range(section_left, section_right)))]['lab']
