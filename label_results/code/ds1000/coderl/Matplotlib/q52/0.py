# SOLUTION END

# Plot y over x
# move the y axis ticks to the right
# SOLUTION START

# x axis labels
ax = plt.subplot(111)
df = pd.DataFrame({"x":x, "y":y})
df.plot.bar(x='x', y='y')
ax.set_ybound(bottom=0)

# SOLUTION END
