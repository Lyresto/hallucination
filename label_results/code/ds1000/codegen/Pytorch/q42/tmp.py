import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import numpy as np
import pandas as pd
import torch

softmax_output = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
### BEGIN SOLUTION
softmax_output = torch.tensor(softmax_output)
softmax_output = softmax_output.view(softmax_output.shape[0], -1)
softmax_output = softmax_output.numpy()
softmax_output = softmax_output.reshape(softmax_output.shape[0], 3)
softmax_output = softmax_output.transpose()
softmax_output = softmax_output.reshape(softmax_output.shape[0], 1)
softmax_output = softmax_output.tolist()
softmax_output = np.array(softmax_output)
softmax_output = softmax_output.reshape(softmax_output.shape[0], 1)
softmax_output = softmax_output.tolist()
softmax_output = np.array(softmax_output)
softmax_output = softmax_output.reshape(softmax_output.shape[0], 1)
softmax_output = softmax_output.tolist()
softmax_output = np.array(softmax_output)
softmax_output = softmax_output.reshape(softmax_output.shape[0], 1)
softmax_output = softmax_output.tolist()
softmax_output = np.array(softmax_output)
softmax_output = softmax_output.reshape(softmax_output.shape[0], 1)
softmax_output = softmax_output.tolist()
softmax_output = np.array(softmax_output)
softmax_output = softmax_output.reshape(softmax_output.shape[0], 1)
softmax_output = softmax_output.tolist()
softmax_output = np.array(softmax_output)
softmax_output = softmax_output.reshape(softmax_output.shape[0], 1)
softmax_output = softmax_output.tolist()
softmax_output = np.array(softmax_output)
softmax_output = softmax_output.reshape(softmax_output.shape[0], 1)
softmax_output = softmax_output.tolist()
softmax_output = np.array(softmax_output)
softmax_output = softmax_output.reshape(softmax_output.shape[0], 1)
softmax_output = softmax_output.tolist()
softmax_output = np.array(softmax_output)
softmax_output = softmax_output.reshape(softmax_output.shape[0], 1)
softmax_output = softmax_output.tolist()
softmax_output = np.array(softmax_output)
softmax_output = softmax_output.reshape(softmax_output.shape[0], 1)
softmax_output = softmax_output.tolist()
softmax_output = np.array(softmax_output)
softmax_output = softmax_output.reshape(softmax_output.shape[0], 1)
softmax_output = softmax_output.tolist()
softmax_output = np.array(softmax_output)
softmax_output
### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(y, f)
