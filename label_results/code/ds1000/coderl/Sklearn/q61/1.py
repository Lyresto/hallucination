import numpy as np

def solve(features):
	df = pd.DataFrame(np.array(features), columns=['f1', 'f2', 'f3', 'f4', 'f5', 'f6'])
	idx = np.arange(len(df['f1'])+1)
	return np.array([[idx==i for i in df['f1']] for i in range(len(df['f1']))])[:,1]
