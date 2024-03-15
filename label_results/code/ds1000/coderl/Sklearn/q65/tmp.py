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
import numpy as np
import pandas as pd
import sklearn.cluster




def label(matrix, fruit):
    dist = np.sqrt(np.sum(np.square(matrix), axis=1))
    res = sklearn.cluster.AgglomerativeClustering(n_clusters=2).fit_predict(dist)
    return [i for i, c in enumerate(res) if c == fruit][0]





def load_data():
    simM = np.array(pd.read_csv('simulation.csv').values)
    return label(simM, 'fruit1')



### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(cluster_labels, f)
