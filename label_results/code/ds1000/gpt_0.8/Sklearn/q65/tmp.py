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
from sklearn.cluster import AgglomerativeClustering

# Convert similarity matrix to distance matrix
distM = 1 - simM

# Perform hierarchical clustering
clustering = AgglomerativeClustering(n_clusters=2, affinity='precomputed', linkage='average')
clustering.fit(distM)

# Get cluster labels
cluster_labels = clustering.labels_

# Print cluster labels
print(cluster_labels)



### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(cluster_labels, f)
