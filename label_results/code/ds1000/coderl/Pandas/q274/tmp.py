import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df, list_of_my_columns = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
# I think this is a dumb way to do it :)

import pandas as pd
import numpy as np

np.random.seed(10)
data = {}
for i in [chr(x) for x in range(65,91)]:
    data['Col '+i] = np.random.randint(1,100,10)
df = pd.DataFrame(data)
list_of_my_columns = ['Col A', 'Col E', 'Col Z']

# df[Avg] = df['Col A'] + df['Col E'] + df['Col Z']

for i in range(len(list_of_my_columns)):
    # df[Avg] = df[list_of_my_columns[i]] / len(list_of_my_columns)
    df[list_of_my_columns[i]] = df[list_of_my_columns[i]].mean()




###END SOLUTION
result = df

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)