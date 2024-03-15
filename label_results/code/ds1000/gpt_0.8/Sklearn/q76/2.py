from sklearn.model_selection import train_test_split

# Split dataset into train and test sets (80/20)
train_data, test_data = train_test_split(dataset, test_size=0.2, random_state=42)

# Split train and test sets into x (features) and y (target)
x_train = train_data.iloc[:, :-1] # select all columns except the last one
y_train = train_data.iloc[:, -1] # select the last column

x_test = test_data.iloc[:, :-1]
y_test = test_data.iloc[:, -1]
END SOLUTION