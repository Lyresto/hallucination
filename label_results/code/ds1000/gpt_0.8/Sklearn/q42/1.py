importance = clf.feature_importances_
mask = importance > np.mean(importance)
selected_columns = X.columns[mask]
column_names = selected_columns.tolist()
