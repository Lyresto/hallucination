result = np.zeros((N,N))
for i in range(N):
    for j in range(N):
        if i == 0:
            result[i,j] = np.sqrt(1/N)
        else:
            result[i,j] = np.sqrt(2/N) * np.cos((np.pi/N) * (j + 0.5) * i)
