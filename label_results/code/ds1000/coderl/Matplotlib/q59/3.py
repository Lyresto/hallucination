def __starting_point():
	df = pd.DataFrame({"X": x, "Y": y})
	ax = df.plot(kind="line", x="X")
	ax.set_xlabel("X")
	ax.set_ylabel("Y")
	# print(df.plot(kind="line", x="Y", y="Z"))
	# # SOLUTION END
	return(fig)

__starting_point()
