# SOLUTION START
def plot_line(x,y,p=1,l=7):
	# In plt.plot(x,y), use a plus marker and give it a thickness of 7
	# SOLUTION END
	if not p:
		p = 1
	l = max(l,7)
	l = max(l,len(str(x).split(' ')[0]))
	l = max(l,len(str(y).split(' ')[0]))
	l = max(l,len(str(x).split(' ')[1]))
	l = max(l,len(str(y).split(' ')[1]))
	return p,l
	
def scatter_matrix(x,y):
	# in plt.plot(x,y), use a plus marker and give it a thickness of 7
	# SOLUTION START
	p,l = plot_line(x,y)
	# in pd.plot(x,y), use a plus marker and give it a thickness of 7
	# SOLUTION END
	p2,l2 = plot_line(x,y,p)
	return p,l,p2,l2
