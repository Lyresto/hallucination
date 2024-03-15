mid = np.array([[shape[0]//2, shape[1]//2]])
y, x = np.indices(shape)
result = distance.cdist(np.dstack((y, x)), mid)
