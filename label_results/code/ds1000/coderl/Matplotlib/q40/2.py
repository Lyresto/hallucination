# remove x axis label
df.y.plot(kind='scatter', x='x')

# remove y axis label
df.x.plot(kind='line', y='y')

# remove x and y axis labels
df.x.plot(kind='scatter', x='x', y='y', color='#ff0000')
df.y.plot(kind='line', x='x', y='y', color='#0000ff')

# remove x and y axis labels
df.x.plot(kind='scatter', x='x', y='y', color='#0000ff', alpha=0.5)
df.y.plot(kind='line', x='x', y='y', color='#0000ff', alpha=0.5)

# remove x and y axis labels
df.x.plot(kind='line', x='x', y='y', color='#ff0000', linewidth=2)
df.y.plot(kind='line', x='x', y='y', color='#0000ff', linewidth=2)

# remove x and y axis labels
df.x.plot(kind='scatter', x='y', y='x', color='#00ff00', linestyle='--')
df.y.plot(kind='line', x='y', y='x', color='#00ff00', linestyle='--')

# remove x and y axis labels
df.x.plot(kind='line', x='y', y='x', color='#0000ff', alpha=0.5)
df.y.plot(kind='line', x='y', y='x', color='#00ff00', alpha=0.5)

# remove x and y axis labels
df.x.plot(kind='scatter', x='y', y='x', color='#0000ff', alpha=0.5, width=3)
df.y.plot(kind='line', x='y', y='x', color='#0000ff', alpha=0.5, width=3)

# remove x and y axis labels
df.x.plot(kind='line', x='y', y='x', color='#00ff00', width=2)
df.y.plot(kind='line', x