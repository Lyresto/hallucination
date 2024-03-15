import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df, list_of_my_columns = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
import pandas as pd
import numpy as np


np.random.seed(10)
data = {}
for i in [chr(x) for x in range(65,91)]:
    data['Col '+i] = np.random.randint(1,100,10)
df = pd.DataFrame(data)
list_of_my_columns = ['Col A', 'Col E', 'Col Z']

###END SOLUTION
result = df

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)