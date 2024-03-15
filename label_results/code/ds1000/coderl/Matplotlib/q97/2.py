# df = pd.DataFrame(values, columns=["Type A", "Type B"], index=["Index 1", "Index 2"])
# label the x axis and y axis in this plot as "X" and "Y"
# SOLUTION END

ax = df.plot(kind='line', x='Index 1', y='Index 2')
ax.set_xlabel('Index 1')
ax.set_ylabel('Index 2')

# SOLUTION START
# df = pd.DataFrame(values, columns=["Type A", "Type B"], index=["Index 1", "Index 2"])
# label the x axis and y axis in this plot as "X" and "Y"
# SOLUTION END

# SOLUTION START
# values = [[1, 2], [3, 4]]
# df = pd.DataFrame(values, columns=["Type A", "Type B"], index=["Index 1", "Index 2"])
# label the x axis and y axis in this plot as "X" and "Y"
# SOLUTION END
