import torch

def predict_allCharacters(input):
	output = MyNet(input)
	conf, classes = torch.max(output.reshape(1, 3), 1)
	class_names = '012'
	return conf, class_names[classes.item()]
