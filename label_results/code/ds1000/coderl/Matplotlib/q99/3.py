import numpy as np

def hatch_plot(x, y):
	hatch = np.hstack((x, y))
	hatch_len = len(hatch)
	hatch_coords = (np.arange(0, hatch_len), np.arange(0, hatch_len))
	hatch_dict = {v: k for k, v in zip(hatch_coords, hatch)}
	return hatch_dict

def scatter_plot(x, y):
	hatches = hatch_plot(x, y)
	return [hatches.get(i) for i in range(x.shape[0])]

def df_to_text(df):
	return pd.Series(df).plot(x='x', y='y', color='r').set_index('x').plot(x='y', y='x')
