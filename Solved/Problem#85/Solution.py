# Testing part

def remove_zero_nodes(tree):
    if tree.root != None:
        if __remove_zero_nodes(tree.root):
            tree.root = None

def __remove_zero_nodes(cur_node):
    if cur_node.left_child != None:
        if __remove_zero_nodes(cur_node.left_child):
            cur_node.left_child = None
    if cur_node.right_child != None:
        if __remove_zero_nodes(cur_node.right_child):
            cur_node.right_child = None
    if cur_node.left_child == None and cur_node.right_child == None:
        if cur_node.value == 0:
            return True

# Solution part

class node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

class Tree:
    def __init__(self):
        self.root = None

    def show_tree(self):
        if self.root != None:
            self.__show_tree(self.root)

    def __show_tree(self, cur_node):
        print(cur_node.value)
        if cur_node.left_child != None:
            self.__show_tree(cur_node.left_child)
        if cur_node.right_child != None:
            self.__show_tree(cur_node.right_child)

tree = Tree()
tree.root = node(0)
tree.root.left_child = node(1)
tree.root.right_child = node(0)
tree.root.right_child.left_child = node(1)
tree.root.right_child.right_child = node(0)
tree.root.right_child.left_child.left_child = node(0)
tree.root.right_child.left_child.right_child = node(0)

print('before removing zero nodes')
tree.show_tree()

remove_zero_nodes(tree)

print('\n\nafter removing zero nodes')
tree.show_tree()
