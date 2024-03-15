from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LogisticRegression


def load_data():
	return np.array(zip(*load_csv(delim=' ')).T)[:,0], np.array(load_csv(delim=' ')).T[:,1]


def load_csv(delim=' ', start=0):
	return pd.read_csv(delim.join((str(start), delim)), delim=delim)
