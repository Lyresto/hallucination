def main():
	# make a two columns and one row subplots
	# Plot y over x in each subplot
	# Give plot a global title "Figure"
	df = pd.DataFrame({"A": x, "B": y})
	# make a row plot
	df.plot(x="A", y="B")
	# make a column plot
	df.plot(x="B", y="A")
	# Give plot a global title "Figure"
	fig = plt.gcf()
	# SOLUTION END
	return fig

def __starting_point():
	main()

__starting_point()
