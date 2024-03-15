# Get the current steps
steps = clf.named_steps

# Delete the 'poly' step from the pipeline
del steps['poly']

# Verify the updated steps
print(clf.named_steps)

# Output: {'reduce_dim': PCA(), 'svm': SVC()}
