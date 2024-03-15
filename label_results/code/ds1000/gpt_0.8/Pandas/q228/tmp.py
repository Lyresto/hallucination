import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

a,b = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
import pandas as pd
import numpy as np
from itertools import zip_longest

# Define the dataframes
a = pd.DataFrame(np.array([[1, 2],[3, 4]]), columns=['one', 'two'])
b = pd.DataFrame(np.array([[5, 6],[7, 8],[9, 10]]), columns=['one', 'two'])

# Create a list of the dataframes
dataframes = [a, b]

# Use zip_longest to iterate over the dataframes simultaneously, filling missing values with np.nan
result = pd.DataFrame(list(zip_longest(*[df.itertuples(index=False) for df in dataframes], fillvalue=np.nan)), columns=a.columns)



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)