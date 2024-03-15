from collections import OrderedDict

def equalp(x, y):
	return True if (isinstance(x, pd.DataFrame) and isinstance(y, pd.DataFrame)) else False
