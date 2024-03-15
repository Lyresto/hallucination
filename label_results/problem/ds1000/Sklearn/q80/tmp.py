import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
### BEGIN SOLUTION
f1 = df['mse'].values.reshape(-1, 1)
kmeans = KMeans(n_clusters=2).fit(f1)
labels = kmeans.predict(f1)
centroids = kmeans.cluster_centers_

### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(labels, f)
