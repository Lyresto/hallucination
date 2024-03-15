import numpy as np
from scipy.spatial.distance import pdist
import pandas as pd
df = pd.read_csv('los_10_one_encoder.csv')
y = df['LOS'] # target
X = df.drop('LOS',axis=1) # drop LOS column
clf = ExtraTreesClassifier(random_state=42)
clf = clf.fit(X,y)
print(clf.feature_importances_)

def get_feature_names(df,col_num):
	# print(f'col_num={col_num}')
	if col_num == 0:
		return list(df.columns)
	k = 2**(col_num-1).bit_length()-1
	feature_names = []
	for i in range(k):
		dist = pdist(df[i],'cityblock')
		# print(dist)
		count = np.sum(dist == 'cityblock')
		# print(f'{i} {count} {dist}')
		count_name = f'{i} {count} {dist}'
		if count!= 0:
			feature_names.append(count_name)
	return feature_names
