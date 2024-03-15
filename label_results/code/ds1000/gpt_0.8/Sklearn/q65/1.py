from sklearn.cluster import AgglomerativeClustering

# Compute the hierarchical clustering
model = AgglomerativeClustering(n_clusters=2, affinity='precomputed', linkage='complete')
cluster_labels = model.fit_predict(simM)

# Convert the cluster labels to a list
cluster_labels = cluster_labels.tolist()
