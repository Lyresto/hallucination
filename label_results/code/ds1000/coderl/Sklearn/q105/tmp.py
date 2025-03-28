import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

features_dataframe = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
### BEGIN SOLUTION
import numpy as np
import pandas as pd




def split_train_test(df):
    train, test = pd.DataFrame(), pd.DataFrame()
    for i, j in enumerate(df.index):
        if i % len(df) == 0:
            train[j] = df[i]
        else:
            test[j] = df[i]
    return train, test



### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump((train_dataframe, test_dataframe), f)
