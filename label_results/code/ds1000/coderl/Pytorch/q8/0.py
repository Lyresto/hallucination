from scipy import ndimage.measurements

def get_data():
	return pd.DataFrame({
		"Index": list(range(6)), 
		"Value": ndimage.convolve(np.ones(6) * 2 - 1, x, mode="nearest").astype(int)
	})
