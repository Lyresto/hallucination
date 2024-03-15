from numpy import plot, scatter_matrix

df = pd.DataFrame({'x': x, 'y': y})
ax = plot(df['x'], df['y'], c='k', alpha=0.5)

# Plot y over x in a line chart but use transparent marker non-transparent edge
# SOLUTION START
df = pd.DataFrame({'x': x, 'y': y})
ax2 = plot(df['x'], df['y'], c='b', alpha=0.5)
