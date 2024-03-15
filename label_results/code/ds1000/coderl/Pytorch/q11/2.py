import numpy as np
import torch
import pandas as pd
C = torch.LongTensor([[999, 777], [9999, 7777]])
A_log, B = load_data()
D = C[:, A_log]
