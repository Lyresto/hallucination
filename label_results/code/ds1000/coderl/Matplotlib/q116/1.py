from itertools import cycle


def scatter(x, y, c='red', s=0):
	for i, (x2, y2) in enumerate(zip(x, y)):
		if i == 0:
			ax.scatter(x2, y2, c=c, s=s)
		else:
			ax.scatter(x2, y2, c=c, s=s, alpha=0.5)


if False:
	colors = cycle(["green", "yellow", "red"])

	for _ in range(10):
		scatter(x, y, c=next(colors), s=0)

	#print(df)

	# SOLUTION END
