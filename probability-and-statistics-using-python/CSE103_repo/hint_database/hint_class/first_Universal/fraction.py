from hint_class_helpers.get_numerical_answer import get_numerical_answer

def check_attempt(p):
	att = get_numerical_answer(p['att_tree'])
	ans = get_numerical_answer(p['ans_tree'])

	if float(ans).is_integer() and not float(att).is_integer():
	   return "Can the number of strings satisfying the constraint be fractional?"
	return ""