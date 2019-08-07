# Solution part

def find_sum_of_contigious_element(lst, k):
	for i in range(len(lst)):
		if lst[i] > k:
			continue
		elif lst[i] == k:
			return [lst[i]]
		else:
			tmp_lst = []
			cur_sum = lst[i]
			tmp_lst.append(lst[i])
			for j in lst[i+1:]:
				cur_sum += j
				tmp_lst.append(j)
				if cur_sum == k:
					return tmp_lst
				elif cur_sum > k:
					break

# Testing part

print(find_sum_of_contigious_element([1, 3, 9, 2, 3, 0], 5))
