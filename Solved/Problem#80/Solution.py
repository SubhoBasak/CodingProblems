# Solution part

def is_matchable(st1, st2):
	lst = list(st1)
	for i in range(len(st2)-1):
		cur = st2[i]
		nxt = st2[i+1]

		indx = lst.index(cur)
		if indx+1 < len(lst) and lst[indx+1] == nxt:
			continue
		elif indx+1 == len(lst) and lst[0] == nxt:
			continue
		else:
			return False
	cur = st2[len(st2)-1]
	nxt = st2[0]
	
	indx = lst.index(cur)
	if indx+1 < len(lst):
		if lst[indx+1] != nxt:
			return False
	elif indx+1 == len(lst):
		if lst[0] != nxt:
			return False
	return True

# Testing part

print(is_matchable('abcdef', 'cdefab'))
print(is_matchable('cdaef', 'adefb'))
