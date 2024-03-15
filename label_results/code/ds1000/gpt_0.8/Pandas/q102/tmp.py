import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np




def f(df):
    ### BEGIN SOLUTION
    import pandas as pd
    
    example_df = pd.DataFrame({'A': ['Good &AMP; bad', 'BB', 'CC', 'DD', 'Good &AMP; bad'], 'B': range(5), 'C': ['Good &AMP; bad'] * 5})
    
    


def f(df):
    df = df.apply(lambda x: x.str.replace('&AMP;', '&', regex=False))
    return df

result = f(example_df)
result


    ### END SOLUTION


df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
result = f(df)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)