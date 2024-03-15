# SOLUTION END


def __starting_point():
	H = np.arange(0,10*10).reshape(10,10)
	plt.imshow(H, cmap=plt.cm.jet, interpolation='nearest')
	#SOLUTION START
	while True:
		input()

__starting_point()
