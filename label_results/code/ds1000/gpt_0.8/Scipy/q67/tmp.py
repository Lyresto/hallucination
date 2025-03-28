
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import io
from scipy import stats

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
zscore = stats.zscore(df, axis=0)
result = pd.DataFrame(zscore, index=df.index, columns=df.columns)



#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)
