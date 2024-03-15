from sklearn.model_selection import train_test_split

# Splitting the dataset into train and test sets
train_set, test_set = train_test_split(dataset, test_size=0.2, random_state=42)

# Splitting the train and test sets into x and y
x_train = train_set.iloc[:, :-1]
y_train = train_set.iloc[:, -1]

x_test = test_set.iloc[:, :-1]
y_test = test_set.iloc[:, -1]
END SOLUTION