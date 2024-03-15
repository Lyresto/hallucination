result = np.empty((a.shape[0]//2, a.shape[1]//2, 2, 2))

for i in range(0, a.shape[0], 2):
    for j in range(0, a.shape[1], 2):
        result[i//2, j//2, :, :] = a[i:i+2, j:j+2]
