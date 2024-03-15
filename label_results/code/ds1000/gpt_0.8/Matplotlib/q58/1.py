plt.figure(figsize=(10, 6))

plt.bar(df['celltype'], df['s1'], label='s1')
plt.bar(df['celltype'], df['s2'], label='s2')

plt.xlabel('celltype')
plt.xticks(rotation=45)

plt.legend()

plt.show()