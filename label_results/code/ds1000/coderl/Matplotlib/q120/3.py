import math

def phi(x):
	return math.factorial(x)

df = pd.DataFrame({"x":x, "y":y})
ax = df.plot.bar(y=phi(x))
ax.set_title("y = x", color="g", fontsize=14)

# SOLUTION END
