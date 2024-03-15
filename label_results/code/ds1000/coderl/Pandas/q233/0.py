import pandas as pd

def merge_rows(df):
	new_df = pd.DataFrame({'text': df['text']})
	for col in df.columns:
		new_df[col] = list(df[col].values())
	return new_df.to_string()
