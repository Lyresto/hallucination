mid = np.array([(shape[0]/2, shape[1]/2)])
y, x = np.indices(shape)
coords = np.dstack((y, x))
result = distance.cdist(coords, mid)
