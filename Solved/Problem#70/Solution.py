def max_path_sum(tree, val1, val2):
	return __max_path_sum(tree.root, val1, val2)

def __max_path_sum(root, val1, val2):
	if val1 == root.value:
		if val2 < val1:
			x = find_height(root.left_child, val2, 1)
			if x != None:
				return x
		else:
			x = find_height(root.right_child, val2, 1)
			if x != None:
				return x
	elif val2 == root.value:
		if val1 < val2:
			x = find_height(root.left_child, val1, 1)
			if x != None:
				return x
		else:
			x = find_height(root.right_child, val2, 1)
			if x != None:
				return x
	
	if val1 < root.value and val2 < root.value:
		return __max_path_sum(root.left_child, val1, val2)
	elif val1 < root.value and val2 > root.value:
		left_len = right_len = 0
		left_len = find_height(root.left_child, val1, 1)
		right_len = find_height(root.right_child, val2, 1)
		if left_len != None and right_len != None:
			return left_len+right_len
	elif val1 > root.value and val2 < root.value:
		left_len = right_len = 0
		left_len = find_height(root.left_child, val2, 1)
		right_len = find_height(root.right_child, val1, 1)
		if left_len != None and right_len != None:
			return left_len+right_len
	elif val1 > root.value and val2 > root.value:
		return __max_path_sum(root.right_child, val1, val2)

def find_height(root, value, cur_height):
	if root.value == value:
		return cur_height
	elif value < root:
		if root.left_child != None:
			return find_height(root.left_child, value, cur_height+1)
		else:
			return None
	else:
		if root.right_child != None:
			return find_height(root.right_child, value, cur_height+1)
		else:
			return None
