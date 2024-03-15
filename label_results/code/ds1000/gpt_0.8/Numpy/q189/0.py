result = np.where((x == a) & (y == b))[0]
if len(result) > 0:
    result = result[0]
else:
    result = -1
