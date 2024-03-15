import numpy as np

# SOLUTION END


def main():
	df = pd.DataFrame({"x": np.arange(10), "y": y})
	fig = df.plot(kind="bar")
	fig.set_size_inches(4, 4)


def __starting_point():
	main()

__starting_point()
