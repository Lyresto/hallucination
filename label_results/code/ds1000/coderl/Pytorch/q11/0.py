import numpy as np
import torch
A_log, B = load_data()
C = B[:, A_log]
