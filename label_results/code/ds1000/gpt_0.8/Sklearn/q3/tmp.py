import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris

data = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))



def solve(data):
### BEGIN SOLUTION
    There is no direct method in pandas to convert a Bunch object to a DataFrame. However, you can convert it using the following steps:
    
    1. Convert the Bunch object to a dictionary.
    2. Convert the dictionary to a DataFrame.
    
    Here is an example of how you can do this:
    
    <code>
    import numpy as np
    from sklearn.datasets import load_iris
    import pandas as pd
    
    # Load the iris dataset
    data = load_iris()
    
    # Convert the Bunch object to a dictionary
    data_dict = {
        'data': data.data,
        'target': data.target,
        'target_names': data.target_names,
        'feature_names': data.feature_names,
        'DESCR': data.DESCR
    }
    
    # Convert the dictionary to a DataFrame
    data_df = pd.DataFrame(data_dict)
    
    print(data_df.head())
    


### END SOLUTION
data1 = solve(data)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(data1, f)
