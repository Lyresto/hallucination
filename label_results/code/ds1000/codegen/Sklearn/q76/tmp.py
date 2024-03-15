import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import pandas as pd
import numpy as np

dataset = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
### BEGIN SOLUTION
import numpy as np
import pandas as pd
dataset = load_data()
x_train, x_test, y_train, y_test =... # put solution in these variables
BEGIN SOLUTION

### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump((x_train, x_test, y_train, y_test), f)
