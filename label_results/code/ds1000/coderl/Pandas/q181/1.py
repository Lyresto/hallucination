from datetime import datetime

def fillna(df, dict_, key=None):
	# fill_value = np.nan
	df[key or 'Member'] = df['Member'].apply(lambda x: dict_.get(x,np.nan))
	
	return df
