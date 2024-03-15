def elementwise_function(element_1,element_2):
	return element_1 + element_2

z = [[4, 4, 4],
	[4, 4, 4],
	[4, 4, 4]]
for i in range(0,4):
	for j in range(0,4):
		z[i][j]=elementwise_function(z[i][j],z[i][j+1])
