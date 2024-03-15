from sklearn.model_selection import train_test_split

# Splitting the dataset into training and testing sets
train_data, test_data = train_test_split(dataset, test_size=0.2, random_state=42)

# Splitting the training set into x_train and y_train
x_train = train_data.iloc[:, :-1]
y_train = train_data.iloc[:, -1]

# Splitting the testing set into x_test and y_test
x_test = test_data.iloc[:, :-1]
y_test = test_data.iloc[:, -1]
END SOLUTION
