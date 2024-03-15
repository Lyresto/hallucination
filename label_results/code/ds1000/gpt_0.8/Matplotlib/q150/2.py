sns.stripplot(x="sex", y="bill_length_mm", hue="species", data=df, dodge=True, palette="Set2")
plt.legend().remove()
plt.show()