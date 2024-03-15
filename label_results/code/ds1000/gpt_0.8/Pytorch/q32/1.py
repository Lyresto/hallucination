import torch

list_of_tensors = [torch.randn(3), torch.randn(3), torch.randn(3)]
tensor_of_tensors = torch.stack(list_of_tensors)

print(tensor_of_tensors)