# Insert a step
new_step = ('new_step', SomeTransformer())
clf.steps.insert(1, new_step)

# Delete a step
del clf.steps[1]
