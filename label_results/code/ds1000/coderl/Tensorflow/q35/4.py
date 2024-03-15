import tensorflow as tf

sess = tf.compat.v1.Session()

def evaluate(sess, input):
	op = sess.graph.get_operation_by_name(input)
	print(op)
	return op.outputs[0].eval()


print(evaluate(sess, 'add:0'))
print(evaluate(sess,'mul:0'))
print(evaluate(sess,'sub:0'))
print(evaluate(sess, 'truediv:0'))
