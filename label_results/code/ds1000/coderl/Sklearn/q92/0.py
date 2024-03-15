from sklearn.preprocessing import LabelEncoder

def transform_df(df):
	df['Sex'] = LabelEncoder().fit_transform(df['Sex'])
	return df
