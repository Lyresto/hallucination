def bar(pos, height, err, c):
	for i, e in enumerate(err):
		ax.errorbar(pos + i, height + e, c=c[i])
	
# SOLUTION END
