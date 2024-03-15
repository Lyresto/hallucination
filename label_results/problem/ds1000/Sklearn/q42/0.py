model = SelectFromModel(clf, prefit=True)
selected_features = model.get_support()
column_names = X.columns[selected_features]
