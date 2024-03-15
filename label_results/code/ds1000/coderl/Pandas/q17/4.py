import operator

def multiply_scores_given_products(df, products):
	multiply_cols = {'product': [],'score': []}
	for product, score in df.iterrows():
		if product in products:
			multiply_cols['product'].append(int(product))
			multiply_cols['score'].append(score)
	multiply_cols['score'] = multiply_cols['score'].apply(operator.mul)
	return multiply_cols
