from itertools import cycle

def scatter(x, y):
	res = [0] * len(x)
	for (i,j) in zip(x,y):
		res[i] = j
	return res

def plot_two_subplots(df):
	fig = df.plot(x='x', y='y', figsize=(15,15))
	for i in cycle(range(2)):
		fig.set_size_inches((15,15))
		yield fig
		
def plot_two_subplots_frame(df):
	fig = pd.DataFrame(df)
	fig.plot(x='x', y='y', figsize=(15,15))
	for i in cycle(range(2)):
		fig.set_size_inches((15,15))
		yield fig

