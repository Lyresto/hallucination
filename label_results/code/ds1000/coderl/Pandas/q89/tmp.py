import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df1, df2, columns_check_list = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
import pandas as pd
df1 = pd.DataFrame({'A': [1, 1, 1],
                  'B': [2, 2, 2],
                  'C': [3, 3, 3],
                  'D': [4, 4, 4],
                  'E': [5, 5, 5],
                  'F': [6, 6, 6],
                  'Postset': ['yes', 'no']})
df2 = pd.DataFrame({'A': [1, 1, 1],
                 'B': [2, 2, 2],
                 'C': [3, 3, 3],
                 'D': [4, 4, 4],
                 'E': [5, 5, 5],
                 'F': [6, 6, 6],
                 'Postset': ['yes', 'no']})
columns_check_list = ['A','B','C','D','E','F']



def check_column_uniqueness(df1,df2):
    result = []
    for column in columns_check_list:
        check = np.where([df1[column]!= df2[column] for column in columns_check_list]) 
        if len(check) > 0:
            result.append(check[0][0])
    return result



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)