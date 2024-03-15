import numpy as np
import pandas as pd
import torch

def convert_to_tensors(list_of_tensors):
	return [torch.tensor(t) for t in list_of_tensors]
