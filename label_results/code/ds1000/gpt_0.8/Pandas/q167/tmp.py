import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
import pandas as pd
import numpy as np

df = pd.DataFrame({'a':[12,13,23,22,23,24,30,35,55], 'b':[1,1,1,2,2,2,3,3,3]})

stdMean = lambda x: pd.Series({'mean': np.mean(x), 'std': np.std(x)})
result = df.groupby('b')['a'].apply(stdMean)
print(result)



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)