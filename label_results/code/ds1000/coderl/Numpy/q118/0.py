def elementwise_function(element_1,element_2):
	return (element_1 + element_2)

z = [[5, 5, 5],
     [5, 5, 5],
     [5, 5, 3]]
for i in range(0,3):
	for j in range(0,3):
		z[i][j] = elementwise_function(x[i][j],y[i][j])
