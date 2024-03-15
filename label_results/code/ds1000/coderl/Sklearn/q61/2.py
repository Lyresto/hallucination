import numpy as np
def solve(features):
	# features = pd.DataFrame.from_records(zip(*features))
	# features = features.apply(lambda row: len(set(row)), axis=1)
		# features = np.array(list(features.values)).astype(int)
		# features = np.hstack([features, features.astype(int)])
		# features = np.hstack([features.values[:-1], [0]])
		sklearn.combination.pivot_table(features, index=0, values='0')
		return features[:,0]
