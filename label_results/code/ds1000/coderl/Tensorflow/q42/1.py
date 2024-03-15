import tensorflow as tf

seed_x = 10

# set the random seed to seed_x with tf.random.ser_seed
seed_x = np.uint32(seed_x)

def sample(size):
	seed_x.shuffle(list(range(len(list(sample(size)))))
	return [seed_x.bit_length() - 1 - i for i in range(size)]
