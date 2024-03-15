from sklearn.cluster import AgglomerativeClustering

clustering = AgglomerativeClustering(n_clusters=2, affinity='precomputed', linkage='complete')
cluster_labels = clustering.fit_predict(data_matrix)
