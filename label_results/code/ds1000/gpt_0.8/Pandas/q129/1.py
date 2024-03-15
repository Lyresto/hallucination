import pandas as pd

df = pd.DataFrame({'UserId': [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3],
                   'ProductId': [1, 4, 7, 4, 2, 1, 1, 4, 7, 4, 2, 1, 1, 4, 7],
                   'Quantity': [6, 1, 3, 2, 7, 2, 6, 1, 3, 2, 7, 2, 6, 1, 3]})

def random_select(df):
    result = []
    for user_id in df['UserId'].unique():
        user_df = df[df['UserId'] == user_id]
        num_rows = int(len(user_df) * 0.2)
        selected_rows = user_df.sample(n=num_rows, random_state=0)
        selected_rows['Quantity'] = 0
        result.append(selected_rows)
    result = pd.concat(result)
    return result

df = random_select(df)
df