import numpy as np

df = pd.DataFrame(dict(zip(x, y)), index=x)
df.plot.boxplot(column=1, row=1)
# yell' on the kata!
