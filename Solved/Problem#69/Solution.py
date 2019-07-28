max_size = 0

def largest_bst(tree):
	global max_size
	if tree.root != None:
	__largest_bst(tree.root)
	return max_size

def __largest_bst(cur_node):
	global max_size
	x = check_bst(cur_node, 1)
	if x != None and x > max_size:
		max_size = x
	if cur_node.left_child != None:
		__largest_bst(cur_node.left_child)
	if cur_node.right_child != None:
		__largest_bst(cur_node.right_child)

def check_bst(root, cur_size):
	if root.left_node == None and root.right_node == None:
		return cur_size
	elif root.left_node != None and root.right_node != None:
		if root.left_node.value < root.value and root.right_child.value > root.value:
			x = check_bst(root.left_child, 1)
			y = check_bst(root.right_child, 1)
			if x != None and y != None:
				return x+y+cur_size
		else:
			return None
	elif root.left_child != None:
		if root.left_child.value < root.value:
			x = check_bst(root.left_child, 1)
			return x+cur_size
		else:
			return None
	elif root.right_child != None:
		if root.right_child.value > root.value:
			x = check_bst(root.right_child, 1)
			return x+cur_size
		else:
			return None
