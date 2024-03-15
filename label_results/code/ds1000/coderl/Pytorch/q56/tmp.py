import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import numpy as np
import pandas as pd
import torch

mask, clean_input_spectrogram, output = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
### BEGIN SOLUTION



def load_data():
    mask, clean_input_spectrogram, output = torch.tensor([[0,0,0,0,0,0,0]], dtype=torch.int)
    return output[0,:,:,mask==1]



### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(output, f)
