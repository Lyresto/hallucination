result = np.empty((a.shape[0]//2, a.shape[1]//2, 2, 2))
for i in range(a.shape[0]//2):
    for j in range(a.shape[1]//2):
        patch = a[i*2:(i+1)*2, j*2:(j+1)*2]
        result[i,j] = patch
