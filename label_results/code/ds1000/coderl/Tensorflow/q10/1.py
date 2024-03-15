import tensorflow as tf
t = [[int(x in [1,2,3,4,5,6,7,8,9]) for x in lengths] for lengths in [0,5,6,7,8,9]]
s = [int(x==1) for x in lengths]
with_pad = []
for s1 in t:
	s1 = [s1[i][j] for i in range(len(s1)) for j in range(8)]
	s1 = tf.pad(s1, [0,8], mode='constant')
	with_pad.append(s1)
result = with_pad[0] + with_pad[1]
