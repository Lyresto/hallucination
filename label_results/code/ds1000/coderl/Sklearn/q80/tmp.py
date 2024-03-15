import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
### BEGIN SOLUTION
from sklearn.cluster import KMeans
df = pd.read_csv("generate_csv/all_data_device.csv", parse_dates=["date"])
f1 = df['mse'].values
# generate another list
f2 = list(range(0, len(f1)))
X = np.array(list(zip(f1, f2)))
kmeans = KMeans(n_clusters=2).fit(X)
labels = kmeans.predict(X)
centroids = kmeans.cluster_centers_
#print(centroids)

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(X[:, 0], X[:, 1], c=labels)
ax.scatter(centroids[:, 0], centroids[:, 1], marker='*', c='#050505', s=1000)
#print(labels)




### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(labels, f)
