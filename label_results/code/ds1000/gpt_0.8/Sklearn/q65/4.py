from sklearn.cluster import AgglomerativeClustering

# Convert the similarity matrix to a distance matrix
distM = 1 - simM

# Perform hierarchical clustering
model = AgglomerativeClustering(n_clusters=2, affinity='precomputed', linkage='average')
cluster_labels = model.fit_predict(distM)
