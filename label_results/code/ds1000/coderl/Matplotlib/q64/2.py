# I think this is not the best practice solution, but it is easy to read.
# I just did some math on the figure and figure title. Somehow that's not what I expected.

# this code is from Russia with love.
# it is not as easy as defining a grid of points and labels, but it is easy to read.

# I used grid(True) from the bottom, and grid(False) from the top. But this worked,
# so it wasn't easy to read. So I used grid(True) and grid(False).

# however, the idea is to use this approach instead of the default grid(),
# so that the labels are aligned with the points.

# I used grid(), but now it's slightly different. Here's the example:

# the grid():
# [x,y]
# [0,5]
# [1,2]
# [0,10]
# [1,2]
# [0,10]

# and the grid():
# [x,y,z]
# [0,5,0,0]
# [1,2,1,2]
# [0,10,0,0]
# [1,2,1,2]

# and the grid():
# [x,y,z,w]
# [0,5,0,0]
# [1,2,1,2]
# [0,10,0,0]
# [1,2,1,2]
# [0,10,0,0]
# [1,2,1,2]

# We are using x-axes, y-axes, and z-axes as the vertical coordinates
# of the legend. The y-axis is used for the x-axes and z-axes.
# So the x-axes coords will have different x-coords.
# The y-axes coords will have different y-coords.

# Let's look at the grid():

# [x,y,z]
# [0,5,0,0]
# [1,2,1,2]
# [0,10,0,0]
# [1,2,1,2]
# [0,10