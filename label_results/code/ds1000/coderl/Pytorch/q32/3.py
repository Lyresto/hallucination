import numpy as np
import pandas as pd
import torch
tensors = [torch.randn(3) for _ in range(10)]
t = [torch.tensor(tensors) for t in tensors]
