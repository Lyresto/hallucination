# SOLUTION END
df = pd.DataFrame({'a':x, 'b':y})
ax = df.plot.bar(y, x)

def main():
	fig = ax.get_figure()
	return fig


def __starting_point():
	main()

__starting_point()
