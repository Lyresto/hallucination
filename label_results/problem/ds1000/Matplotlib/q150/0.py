sns.stripplot(x="sex", y="bill_length_mm", hue="species", data=df, jitter=True)
plt.legend().remove()
plt.show()