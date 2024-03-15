val_cols = [col for col in df.columns if col.startswith('val')]
result = df.groupby('group').agg({"group_color": "first", **{col: "mean" for col in val_cols}})
