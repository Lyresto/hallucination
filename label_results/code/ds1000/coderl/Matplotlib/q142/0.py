from itertools import chain

def pchart(df, x=None, y=None):
	if x is None:
		x = np.arange(10)
	if y is None:
		y = np.arange(10)
	
	return (
		chain(
			df.plot(x=x, y=y).set_xlabels([]).show(xaxis_label=False),
			df.plot(x=x, y=y).set_xlabels([x.min(), x.max()]).show(xaxis_label=True),
		)
	)
