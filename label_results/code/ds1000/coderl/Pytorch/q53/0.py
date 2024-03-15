import numpy as np
import pandas as pd
import torch
A, B = load_data()
cnt_not_equal = torch.equal(A,B).sum()
