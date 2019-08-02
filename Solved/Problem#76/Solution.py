def find_minimun_steps(lst):
	x1, y1 = lst[0]
	total_steps = 0
	for x2, y2 in lst[1:]:
		if abs(x1-x2) < abs(y1-y2):
			x = abs(x1-x2)
			total_steps += x+(abs(y1-y2)-x)
		else:
			y = abs(y1-y2)
			total_steps += y+(abs(x1-x2)-y)
		x1 = x2
		y1 = y2
	return total_steps

print(find_minimun_steps([(1, 5), (3, 1), (5, 5), (9, 6)]))
