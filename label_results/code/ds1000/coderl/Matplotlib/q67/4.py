# SOLUTION START

# MAKE SCALARPLOT
a_s = np.array(a)
b_s = np.array(b)
c_s = np.array(c)

fig, ax = plt.subplots()
ax.scatter(a_s, b_s)
for i, x in enumerate(c_s):
	ax.annotate(str(i), (x, i))

# SAVE AND GRAPH
ax.set_xlabel('x')
ax.set_ylabel('y')

# SOLUTION END
