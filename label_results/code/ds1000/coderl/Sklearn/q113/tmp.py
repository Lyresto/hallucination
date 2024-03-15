import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import pandas as pd
import numpy as np

if os.path.exists("sklearn_model"):
    os.remove("sklearn_model")



def creat():
    import pickle

    fitted_model = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
    return fitted_model
fitted_model = creat()
### BEGIN SOLUTION
import numpy as np
import pandas as pd




def isit(X, Y, model):
    return np.sum((Y - model.predict(X)) ** 2, axis = 0)




def save_data():
    return pd.Series({'weights':isit(X,Y,fitted_model),'means':isit(X,Y,fitted_model.mean()),'covs':isit(X,Y,fitted_model.cov())})



### END SOLUTION
if os.path.exists("sklearn_model") and not os.path.isdir("sklearn_model"):
    import pickle

    with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
        pickle.dump("accept", f)
else:
    import pickle

    with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
        pickle.dump("reject", f)
