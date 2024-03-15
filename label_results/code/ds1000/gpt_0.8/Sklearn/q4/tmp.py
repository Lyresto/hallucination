import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import pandas as pd
import numpy as np
import sklearn

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
### BEGIN SOLUTION
from sklearn.preprocessing import MultiLabelBinarizer

mlb = MultiLabelBinarizer()
df_out = pd.concat([df, pd.DataFrame(mlb.fit_transform(df['Col3']), columns=mlb.classes_)], axis=1).drop('Col3', axis=1)



### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(df_out, f)
