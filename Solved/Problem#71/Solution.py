def next_val(lst):
	if len(lst) == 2:
		return [lst[1], lst[0]]
	
	val = ''
	for i in lst:
		val += str(i)
	val = int(val)
	
	if len(lst) > 2:
		x = __next_val(lst[1:], val)
		tmp = ''
		for i in [lst[0]]+x:
			tmp += str(i)
		tmp = int(tmp)
		if tmp > val:
			return [lst[0]]+x
		return [lst[0]]+x

def __next_val(due, val):
	if len(due) == 2:
		return [due[1], due[0]]
	elif len(due) > 2:
		x = __next_val(due[1:], val)
		tmp = ''
		for i in [due[0]]+x:
			tmp += str(i)
		tmp = int(tmp)
		if tmp > val:
			return [due[0]]+x
		return [due[0]]+x
