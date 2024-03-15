To calculate the cumulative average for each row from end to head while ignoring zero values, you can use the following code:

<code>
df = df.set_index('Name')  # Set 'Name' column as index
df = df.apply(lambda x: x[::-1].cumsum()[::-1] / (x != 0)[::-1].cumsum()[::-1])  # Calculate cumulative average while ignoring zero values
df = df.reset_index()  # Reset index to bring 'Name' column back
