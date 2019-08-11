# Solution part

class queue:
	def __init__(self):
		self.__items = []

	def enqueue(self, value):
		self.__items.append(value)

	def dequeue(self):
		return self.__items.pop(0)

	def is_empty(self):
		if len(self.__items) == 0:
			return True
		return False

q = queue()

def level_view(tree):
	if tree.root != None:
		q.enqueue(tree.root)
		__level_view()

def __level_view():
	cur_node = q.dequeue()
	print(cur_node.value)
	if cur_node.left_child != None:
		q.enqueue(cur_node.left_child)
	if cur_node.right_child != None:
		q.enqueue(cur_node.right_child)
	if not q.is_empty():
		__level_view()

# Testing part

class node:
	def __init__(self, value):
		self.value = value
		self.left_child = None
		self.right_child = None

class tree:
	def __init__(self):
		self.root = None
	
	def add(self, value):
		if self.root == None:
			self.root = node(value)
		else:
			self.__add(self.root, value)
	
	def __add(self, cur_node, value):
		if value < cur_node.value:
			if cur_node.left_child != None:
				self.__add(cur_node.left_child, value)
			else:
				cur_node.left_child = node(value)
		elif value > cur_node.value:
			if cur_node.right_child != None:
				self.__add(cur_node.right_child, value)
			else:
				cur_node.right_child = node(value)
		else:
			print('Value already in tree !')

Tree = tree()
for i in [5, 2, 10, 1, 4, 8, 0, 3, 6, 9, 7]:
	Tree.add(i)

level_view(Tree)
