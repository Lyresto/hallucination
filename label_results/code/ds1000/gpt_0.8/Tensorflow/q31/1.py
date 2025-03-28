```python
result = [s.decode('utf-8') for s in x]
return result
```

You can use the `decode` function with the encoding 'utf-8' to convert each byte string in the list `x` to a string. This can be done using a list comprehension to iterate over each element in `x` and apply the `decode` function. The resulting list will contain the decoded strings.