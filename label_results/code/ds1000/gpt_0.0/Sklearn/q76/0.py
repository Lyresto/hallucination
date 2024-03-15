# Splitting dataset into training and testing sets
from sklearn.model_selection import train_test_split

X = dataset.iloc[:, :-1] # all columns except the last one
y = dataset.iloc[:, -1] # only the last column

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

