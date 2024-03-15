import math
def predict_allCharacters(input):
	output = MyNet(input)
	return [math.log(output[i, j] / output[i, :].sum()).real for j in range(15)]
