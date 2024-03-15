def merge_rows(df):
	text = df['text']
	text_array = list(text)
	res = text_array[0]
	new_row = text_array[0]
	for i in range(1, len(text_array)):
		if text_array[i]!= res:
			res = text_array[i]
			new_row = text_array[i]
	text_array.remove(res)
	text_array.append(new_row)
	return text_array
