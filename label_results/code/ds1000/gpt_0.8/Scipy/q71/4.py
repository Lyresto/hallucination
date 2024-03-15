mid = np.array([shape[0]//2, shape[1]//2])  # center point
y, x = np.meshgrid(np.arange(shape[0]), np.arange(shape[1]))  # create meshgrid of coordinates
coords = np.dstack((y, x))  # stack coordinates along the third axis
result = distance.cdist(coords, mid.reshape(1, 2)).reshape(shape)  # compute distances and reshape to desired shape
