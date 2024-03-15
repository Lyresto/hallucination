from collections import Counter

def load_data():
	A = pd.read_csv('data/A.csv').values
	B = pd.read_csv('data/B.csv').values
	return A, B
