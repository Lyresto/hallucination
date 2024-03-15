import numpy as np
import pandas as pd
import torch
a = torch.rand((10, 1000, 96))
lengths = torch.randint(1000, (10,))
