def __starting_point():
	H = np.rot90(H)
	fig, ax = plt.subplots()
	ax.imshow(H, cmap=plt.cm.jet)
	# SOLUTION END

__starting_point()
