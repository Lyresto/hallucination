result = np.zeros(np.max(index)+1)
for i in range(np.max(index)+1):
    result[i] = np.max(a[index==i])
