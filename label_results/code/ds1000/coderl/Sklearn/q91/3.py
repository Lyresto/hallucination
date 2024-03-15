from sklearn.preprocessing import LabelEncoder

def transform(df):
	df['Sex'] = LabelEncoder().fit_transform(df['Sex'])
	return df
