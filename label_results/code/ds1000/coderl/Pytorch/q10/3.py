import numpy as np
import torch
A_logical, B = load_data()
C = B[:, A_logical]
