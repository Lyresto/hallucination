result = []
for i in range(a.shape[0]-1):
    for j in range(a.shape[1]-1):
        patch = a[i:i+2, j:j+2]
        result.append(patch.tolist())
result = np.array(result)
