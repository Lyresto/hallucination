def zero_out_row_and_column(a):
	# Make sure first column is zero
	col = 0
	for i in range(len(a)):
		if a[0][i] == 0:
			a[0][col] = 0
			col += 1
	# Make sure second row is zero
	row = 0
	for i in a[1:]:
		if a[row][i] == 0:
			a[row][i] = 0
			row += 1
