import numpy as np

a = np.array([[1,5,9,13],
              [2,6,10,14],
              [3,7,11,15],
              [4,8,12,16]])

result = []
for i in range(a.shape[0] - 1):
    for j in range(a.shape[1] - 1):
        patch = a[i:i+2, j:j+2]
        result.append(patch)
        
result = np.array(result)
print(result)
