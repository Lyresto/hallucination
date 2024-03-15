import seaborn as sfg

df = df.copy()
df = df.loc[df["a"] < 21]

# convert df to a seaborn DataFrame
sfg.pointplot(df, x="b", y="c", column="a")

# remove first line, and remove columns
df = df.loc[df["a"]!= 21]

# SAVE AND SAVE LABELS
sfg.despine(left=True)
sfg.light_curves(y="c", x="b")

# SOLUTION END
