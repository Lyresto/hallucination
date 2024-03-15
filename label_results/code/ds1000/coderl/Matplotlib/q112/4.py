# SOLUTION END

# Plot y over x in a line chart but use non-transparent edge
# SOLUTION START
df = pd.DataFrame({"x": x, "y": y})

# Plot y over x
df.plot(x="x", y="y")

# Plot y over x but use non-transparent edge
df.plot(x="x", y="y", marker="^", markersize=3)

# SOLUTION END

# Plot y over x
df.plot(x="y", y="x", marker="^", markersize=2)

# Plot y over x but use non-transparent edge
df.plot(x="y", y="x", marker="^", markersize=1)

# Plot y over x
df.plot(x="y", y="x", marker="^", markersize=0)

# SOLUTION START
df.plot(x="x", y="y", alpha=0.3, zorder=2)

# Plot y over x
df.plot(x="y", y="x", alpha=0.3, marker="^", markersize=0.5)

# Plot y over x
df.plot(x="y", y="x", alpha=0.3, marker="^", markersize=1)

# Plot y over x
df.plot(x="y", y="x", alpha=0.3, marker="^", markersize=2)

# Plot y over x
df.plot(x="y", y="x", alpha=0.3, marker="^", markersize=3)

# SOLUTION START
df.plot(x="y", y="x", c="blue", marker="^", markersize=0.5)

# Plot y over x
df.plot(x="y", y="x", c="blue", marker="^", markersize=1)

# Plot y over x
df.plot(x="y", y="x", c="blue", marker="^", markersize=2)

# Plot y over x
df.plot(x="y", y="x", c="red", marker="^", markersize=0.5)

# Plot y over x