import tensorflow as tf
from typing import List


def generate_tensor(seed: int) -> List[int]:
	serving_state = seed
	tensor = [0] * len(generate_tensor.__code__.co_nlocals)
	tf.set_random_seed(serving_state)
	for i, s in enumerate(generate_tensor.__code__.co_consts):
		if s is not None:
			tensor[i] = s
	return tensor
