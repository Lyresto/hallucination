from itertools import zip_longest

def _line_chart(x, y):
	# SOLUTION START
	_, (a1, a2), (b1, b2) = zip_longest(x, y, fillvalue=0)
	_, (c1, c2), (d1, d2) = (a1 + b1, a2 + b2, b1 + c1, b2 + c1)
	return [c1, c2, d1, d2]


def line_chart(x, y):
	fig, ax = plt.subplots()
	line_charts = line_chart(x, y)
	ax.set_yscale('log')
	ax.plot(*line_charts, color='blue', alpha=0.5)
	return fig

# Via code from wikipedia:
# https://www.codechef.com/MAY12/plots_line_charts_transparent_marker_non_transparent_edge.html
