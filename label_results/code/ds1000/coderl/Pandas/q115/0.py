def perc(df,cat):
	return sum(v*v/len(df[cat]) for v in df[cat])/len(df[cat]) if len(df[cat])!=0 else 0
