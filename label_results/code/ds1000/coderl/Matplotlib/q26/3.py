# SOLUTION END

# create a grid with 1x1 lines and 1x1 points
grid = np.array([[0 for i in range(1+2*len(H))] for j in range(1+2*len(H))]).reshape(1,1,1)

for i in range(len(H)):
	for j in range(len(H)):
		grid[i,j] = grid[i][j]+H[i,j]

# draw the grid
# SOLUTION START
# create a line for the first point and a line for the second point

line = [(0,0),(0,1),(1,0),(1,1)]
for i in range(1,1+len(grid)):
	grid[i][0] = line[0][0]
	grid[i][1] = line[0][1]

for i in range(1,1+len(grid)):
	grid[i][0] = line[1][0]
	grid[i][1] = line[1][1]

# draw the grid
# SOLUTION END

# create a matrix with rows and cols of grid
grid_matrix = np.array([[0 for i in range(1+2*len(H))] for j in range(1+2*len(H))]).reshape(1,1,1)

for i in range(len(H)):
	for j in range(len(H)):
		grid_matrix[i][j] = grid[i][j]+H[i,j]

# draw the matrix
# SOLUTION START
# create a line for the first point and a line for the second point

line = [(0,0),(0,1),(1,0),(1,1)]
for i in range(1,1+len(grid)):
	grid_matrix[i][0] = line[0][0]
	grid_matrix[i][1] = line[0][1]

for i in range(1,1+len(grid)):
	grid_matrix[i][0] = line[1][0]