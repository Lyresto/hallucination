import numpy as np

a = np.array([[1,2,8],
              [7,4,2],
              [9,1,7],
              [0,1,5],
              [6,4,3]])

result = np.zeros((len(a), len(a))) # initialize result matrix

for i in range(len(a)):
    for j in range(len(a)):
        result[i][j] = np.linalg.norm(a[i] - a[j]) # calculate distance using Euclidean norm

END SOLUTION