from sklearn.cluster import KMeans
from itertools import zip_longest
df = pd.read_csv("generate_csv/all_data_device.csv", parse_dates=["date"])
f1 = df['mse'].values
# generate another list
f2 = list(range(0, len(f1)))
X = np.array(list(zip_longest(f1, f2)))
kmeans = KMeans(n_clusters=2).fit(X)
labels = kmeans.predict(X)
centroids = kmeans.cluster_centers_
#print(centroids)

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(X[:, 0], X[:, 1], c=labels)
ax.scatter(centroids[:, 0], centroids[:, 1], marker='*', c='#050505', s=1000)
#print(labels)
#print(centroids)


#BEGIN SOLUTION

'''
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

#fig = plt.figure()
#ax = Axes3D(fig)
#ax.scatter(X[:, 0], X[:, 1], c=labels)
#ax.scatter(centroids[:, 0], centroids[:, 1], marker='*', c='#050505', s=1000)
#print(labels)
#print(centroids)

#INTO SOLUTION

df = pd.read_csv("generate_csv/all_data_device.csv", parse_dates=["date"])
f1 = df['mse'].values
# generate another list
f2 = list