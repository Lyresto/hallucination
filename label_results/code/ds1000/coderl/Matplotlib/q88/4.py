import numpy as np

df = pd.DataFrame({'a': np.arange(10)})
df['b'] = df.a.apply(lambda x: str(x % 2))

# Sometimes pandas can't display the first two x labels, so we have to use the names of the first
# x to change to second x axis label
ax.set_xticklabels(['first','second'])

# # This doesn't work; See https://github.com/matplotlib/matplotlib/issues/26899
# ax.xaxis.label = 'third'

# # This works!
# ax.xaxis.label_format = '%1.1f'

plt.show()
