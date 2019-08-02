def longest_consecutive(lst):
	lst.sort()
	cur_max = 1
	tmp_max = 1
	for i in range(len(lst)-1):
		if lst[i]+1 == lst[i+1]:
			tmp_max += 1
		else:
			if tmp_max > cur_max:
				cur_max = tmp_max
				tmp_max = 1
	return cur_max


print(longest_consecutive([100, 4, 200, 1, 3, 2]))
