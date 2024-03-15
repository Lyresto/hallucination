import numpy as np
import pandas as pd
import torch
MyNet = torch.nn.Sequential(torch.nn.Linear(4, 15),
                            torch.nn.Sigmoid(),
                            torch.nn.Linear(15, 3),
                            )
MyNet.load_state_dict(torch.load("my_model.pt"))
input = load_data()
assert type(input) == torch.Tensor
