from sklearn.cluster import AgglomerativeClustering

model = AgglomerativeClustering(n_clusters=2, affinity='precomputed', linkage='complete')
cluster_labels = model.fit_predict(data_matrix)
