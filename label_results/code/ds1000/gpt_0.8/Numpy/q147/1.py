import numpy as np

post = [2, 5, 6, 10]
distance = [50, 100, 500, 1000]

result = np.corrcoef(post, distance)[0, 1]
result