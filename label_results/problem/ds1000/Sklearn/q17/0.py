Yes, it is possible to insert or delete a step in a sklearn.pipeline.Pipeline object. 

To insert a step, you can use the insert method of the list object returned by the named_steps() method. For example, to insert a PolynomialFeatures step after the PCA step, you can do:

<code>
steps = clf.named_steps
steps.insert(1, ('poly', PolynomialFeatures()))
