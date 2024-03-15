from sklearn.cluster import AgglomerativeClustering

# Create hierarchical clustering model
model = AgglomerativeClustering(n_clusters=2, affinity='precomputed', linkage='average')

# Fit the model to the similarity matrix
model.fit(simM)

# Get the cluster labels
cluster_labels = model.labels_
