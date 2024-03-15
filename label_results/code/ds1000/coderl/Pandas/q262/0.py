def filter_dataframe(df, filt):
	return df.reindex(df.index.append(filt.index).set_index(['a', 'b'])).to_dict('records')
