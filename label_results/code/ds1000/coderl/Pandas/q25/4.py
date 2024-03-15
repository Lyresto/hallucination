from datetime import date
def extract_date(df,s):
	arr = [(date(int(s[0]),int(s[1]),int(s[2]))).strftime('%Y-%m-%d'),]
	for i in range(len(s)-1):
		arr.append(date(int(s[i+1]),int(s[i+2]),int(s[i+3]))).strftime('%Y-%m-%d')
	return arr[0] if arr[0]!= '00-00' else arr[1]
