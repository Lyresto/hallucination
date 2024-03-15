from re import sub

def clean_column(df, name):
	df['SOURCE_NAME'] = sub('_[a-z]*$', '', df['SOURCE_NAME'])
	return df
