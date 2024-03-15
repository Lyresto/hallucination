def line(x,y):
	df = pd.DataFrame({'x':x,'y':y})
	df.plot(x='x',y='y',marker='.',linewidth=2)
	return plt.gcf()
