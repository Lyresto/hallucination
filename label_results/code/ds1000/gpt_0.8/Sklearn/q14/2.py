You can delete a step from the Pipeline object by using the `del` keyword and specifying the step you want to delete. For example, to delete the 'poly' step, you can do:
<code>
del clf.named_steps['poly']
