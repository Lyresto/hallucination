from scipy.stats import anderson
def anderson(*arrays):
	return all(anderson(*a) for a in arrays)
