from itertools import product
from itertools import zip_longest

def polar(labels, heights):
	ax = plt.gca()
	n, m = len(labels), len(heights)
	p1, p2 = ax.polar(zip_longest(labels, heights), fill_between=1, center=0)
	return [p1[i][1] for i in range(n)]
	
def plot_bar_plot(labels, height):
	return plt.bar(*[i*v for i, v in zip_longest(labels, height, fill_between=1)], height=height)
