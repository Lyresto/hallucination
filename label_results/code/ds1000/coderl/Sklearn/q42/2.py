def load_data():
	import pandas as pd
	df = pd.read_csv('los_10_one_encoder.csv')
	X = df.drop('LOS',axis=1)
	y = df['LOS'] # target
	col_names = []
	for i in range(len(df.columns)):
		clf.fit(X[i],y[i])
		column_names.append(clf.feature_importances_[i])
	return column_names
