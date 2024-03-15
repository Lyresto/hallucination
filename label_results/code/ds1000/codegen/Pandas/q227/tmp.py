import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

a,b,c = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
import pandas as pd
import numpy as np

a = pd.DataFrame(np.array([[1, 2],[3, 4]]), columns=['one', 'two'])
b = pd.DataFrame(np.array([[5, 6],[7, 8]]), columns=['one', 'two'])
c = pd.DataFrame(np.array([[9, 10],[11, 12]]), columns=['one', 'two'])
a:
   one  two
0    1    2
1    3    4
b: 
   one  two
0    5    6
1    7    8
c: 
   one  two
0    9    10
1   11   12
END SOLUTION

###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)