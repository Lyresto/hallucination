def line_chart(x, y):
	# Chart code goes here
	plt.plot(x, y, 'o')
	# Set x and y axis labels
	x_label = str(x)
	y_label = str(y)
	# Remove y axis label
	x_label.split()[1] = ''
	y_label.split()[1] = ''
	# Set x axis label and y axis label
	x_label_label = x_label.split()[0]
	y_label_label = y_label.split()[0]
	# Remove the first element
	x_label_label = x_label_label.split()[1]
	y_label_label = y_label_label.split()[1]
	# Show x and y axis labels
	print(x_label)
	print(y_label)
	
	# SOLUTION END
	
	return


def main():
	line_chart(x, y)
	
main()

