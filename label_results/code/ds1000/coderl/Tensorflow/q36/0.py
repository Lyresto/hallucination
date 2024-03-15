from collections import Counter

def test_count():
	c = Counter(a.numpy()[i] for i in range(100))
	assert c['0'] == 1, '0'
	assert c['5'] == 1, '5'
	assert c['7'] == 2, '7'
	assert c['9'] == 1, '9'
