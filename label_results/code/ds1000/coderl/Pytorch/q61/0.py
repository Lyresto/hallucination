from collections import Counter
def predict_allCharacters(input):
	output = MyNet(input)
	return [i[1] for i in Counter(output.reshape(1, 3)).most_common(1)]
