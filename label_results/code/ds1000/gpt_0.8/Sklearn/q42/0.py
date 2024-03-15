model = SelectFromModel(clf, prefit=True)
selected_features = model.get_support(indices=True)
column_names = X.columns[selected_features]
