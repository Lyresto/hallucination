def line_chart(x,y):
	df = pd.DataFrame({'x':x, 'y':y})
	return df.plot.line()

def y_of_x(x, y):
	return x[y]

# Plot y over x in a line chart and name axis with labels (x and y). Hide tick labels but keep axis labels.
# SOLUTION START
y_of_x(x, y)
plt.title('y-of-x')
plt.ylabel('y')

