import numpy as np
import pandas as pd

df = pd.read_csv('los_10_one_encoder.csv')

def transform(x, y, selected):
	new = np.array([])
	for i in range(len(x)):
		if i in selected:
			new[i] = x[i]
		else:
			new[i] = 1
	return new

def run_select_feature():
	clf = ExtraTreesClassifier(random_state=42)
	clf = clf.fit(transform(df, df['LOS'], ['LOS']), df['LOS'])
	print(clf.feature_importances_)

run_select_feature()
