import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import pandas as pd
import numpy as np
import sklearn.cluster

simM = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
### BEGIN SOLUTION
# Convert the similarity matrix to a distance matrix
distM = 1 - np.array(simM)

# Perform hierarchical clustering using complete linkage
agg_clustering = sklearn.cluster.AgglomerativeClustering(n_clusters=2, linkage='complete', affinity='precomputed')
cluster_labels = agg_clustering.fit_predict(distM)

# Print the cluster labels
print(cluster_labels)

### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(cluster_labels, f)
