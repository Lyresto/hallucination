result = np.zeros((len(a), len(a))) # initialize result matrix with zeros
for i in range(len(a)):
    for j in range(len(a)):
        result[i][j] = np.linalg.norm(a[i]-a[j]) # calculate Euclidean distance between i-th and j-th point
