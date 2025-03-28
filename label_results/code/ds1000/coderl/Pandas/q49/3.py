def aggregate_rows_not_in_a_section(df, section_left, section_right):
	sections = [[df[s][i] for i in range(section_left, section_right+1)] for s in df.index]
	return sum(sum(sections[i]) / len(sections[i]) for i in range(section_right-section_left+1)) or 0
