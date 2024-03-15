seaborn.figure(figsize=(8, 8))
seaborn.relplot(df, x="Gender", y="Height (cm)", color="Weight (kg)")
plt.show()
