def permutations(lst):
	if len(lst) == 0:
		return None
	elif len(lst) == 1:
		return lst
	elif len(lst) >= 2:
		op_lst = []
		for i in range(len(lst)):
			x, y = __permutations([lst[i]], lst[:i]+lst[i+1:])
			if y == True:
				op_lst.append(x)
			else:
				op_lst += x
		return op_lst
			

def __permutations(cur, rest):
	if len(rest) == 0:
		return cur, True
	op_lst = []
	for i in range(len(rest)):
		tmp = cur[:]
		x, y = __permutations(tmp+[rest[i]], rest[:i]+rest[i+1:])
		if y == True:
			op_lst.append(x)
		else:
			op_lst += x
	return op_lst, False

for i in permutations([1, 2, 3, 4, 5]):
	print(i)
