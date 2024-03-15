import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import pandas as pd
import numpy as np
import sklearn.cluster

data_matrix = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
### BEGIN SOLUTION
# Convert distance matrix to condensed distance matrix
dist_matrix = np.sqrt(2*(1-np.array(data_matrix)))
condensed_dist_matrix = pdist(dist_matrix)

# Perform hierarchical clustering
agg_clustering = sklearn.cluster.AgglomerativeClustering(n_clusters=2, linkage='average', affinity='precomputed')
agg_clustering.fit_predict(squareform(condensed_dist_matrix))

# Convert cluster labels to list
cluster_labels = agg_clustering.labels_.tolist()

### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(cluster_labels, f)
