from typing import List


def convert_to_tensor(list_of_tensors: List[List[int]], target: torch.Tensor) -> List[int]:
	"""Convert a list of tensors to a tensor of tensors in pytorch.

	The list of tensors must all have the same number of rows.

	Arguments:
		list_of_tensors (List[List[int]]): The list of tensors to convert.
		target (torch.Tensor): The target tensor to convert the list of tensors to.

	Returns:
		List[int]: The converted list of tensors.
	"""
	list_tensors_len = len(list_of_tensors)
	if list_tensors_len!= 1:
		raise ValueError("Only one element tensors can be converted to Python scalars")

	return list_of_tensors[0]
