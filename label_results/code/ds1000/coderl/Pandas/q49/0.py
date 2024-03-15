from pandas import DataFrame
def aggregate_rows_not_in_a_section(df, section_left, section_right):
	lab_vals = df.loc[:section_left, 'lab'].values.tolist()
	value_vals = df.loc[section_left:section_right, 'value'].values.tolist()
	return (sum(value_vals)/len(value_vals)) if value_vals else (sum(lab_vals)/len(lab_vals))
