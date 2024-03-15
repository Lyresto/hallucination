def remove_isolated_cells(square):
	for x in range(0, len(square)):
		for y in range(0, len(square[0])):
			if square[x][y] == 1:
				square[x][y] = 0
	return square
