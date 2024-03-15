#try:
#    import pandas as pd
#    df = pd.DataFrame(
#        {'HeaderA': [476],
#         'HeaderB': [4365],
#         'HeaderC': [457],
#         'HeaderX': [345]})
#except ImportError:
#    pass



def rename_columns(df):
	#your code here
	new_df = df.copy()
	for i in range(len(df.columns)):
		if not any(i[-1] in ['X', 'Y'] for i in df.columns):
			new_df['Header' + i] = [i for i in df.columns if i[-1] not in ['X', 'Y']]
	return new_df
