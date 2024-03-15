plt.figure(figsize=(10, 8))
sns.scatterplot(data=df, x="bill_length_mm", y="bill_depth_mm", s=30)

plt.title("Scatter plot of Bill Length vs Bill Depth")
plt.xlabel("Bill Length (mm)")
plt.ylabel("Bill Depth (mm)")

plt.show()