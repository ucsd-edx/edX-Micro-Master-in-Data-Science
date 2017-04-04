def check_attempt(p):
	if p['att_tree'][0] == 'X' and p['ans_tree'][0] != 'X':
		return "Please write an expression, not the final numerical result."
	return ""