
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import io
from scipy import stats

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import pandas as pd
import io
from scipy import stats

temp=u"""probegenes,sample1,sample2,sample3
1415777_at Pnliprp1,20,0.00,11
1415805_at Clps,17,0.00,55
1415884_at Cela3b,47,0.00,100"""
df = pd.read_csv(io.StringIO(temp),index_col='probegenes')

#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)
