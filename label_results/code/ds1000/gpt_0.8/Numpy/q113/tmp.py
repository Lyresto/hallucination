import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
import pandas as pd
index, columns = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
values = np.zeros((2,3), dtype=[('a', 'int32'), ('b', 'float32'), ('c', 'float32')])
df = pd.DataFrame(values, index=index, columns=columns)



#print(df)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(df, file)
