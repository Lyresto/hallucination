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
import pandas as pd
import numpy as np
import sklearn.cluster




def do():
    matrix = pd.DataFrame(data_matrix)
    dis = matrix.pivot(index='prof', values='distance', columns='prof')
    clust = sklearn.cluster.AgglomerativeClustering(n_clusters=2).fit(dis)
    return clust.labels_



### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(cluster_labels, f)
