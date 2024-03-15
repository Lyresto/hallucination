def errorbar(x, y, yerr):
	x += 0.5*xerr
	y += 0.5*yerr
	return (x, y), ("b", "r")[yerr > 0]

# plot y errors of x with colors in c
x, y = np.linspace(4), np.array([1, 1, 2, 2])
yerr = np.array([0.1, 0.2, 0.3, 0.4])
xerr, yerr = errorbar(x, y, yerr)

# SOLUTION END
