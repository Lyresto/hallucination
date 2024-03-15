# -*- coding: utf-8 -*-

def plot_xy(df, x, y):
	df['X'] = x
	df['Y'] = y
	fig, ax = plt.subplots()
	ax.plot(df['X'], df['Y'])
	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	return fig
