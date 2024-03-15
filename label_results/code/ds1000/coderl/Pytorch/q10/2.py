import numpy as np
import torch

def load_data():
	A_logical, B = torch.LongTensor([[int(i) for i in row] for row in sys.stdin.read().split()]).numpy()[:2]
	return B[:, A_logical]
