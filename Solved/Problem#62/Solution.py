# Solution part

def reverse(tree):
    if tree.root != None:
        __reverse(tree.root)

def __reverse(root):
    tmp = root.left_child
    root.left_child = root.right_child
    root.right_child = tmp
    if root.left_child != None:
        __reverse(root.left_child)
    if root.right_child != None:
        __reverse(root.right_child)

# Testing part

class node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

class Tree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root == None:
            self.root = node(value)
        else:
            self.__add(self.root, value)

    def __add(self, cur_node, value):
        if value < cur_node.value:
            if cur_node.left_child == None:
                cur_node.left_child = node(value)
            else:
                self.__add(cur_node.left_child, value)
        elif value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = node(value)
            else:
                self.__add(cur_node.right_child, value)

    def show_tree(self):
        self.__show_tree(self.root)

    def __show_tree(self, cur_node):
        print(cur_node.value)
        if cur_node.left_child != None:
            self.__show_tree(cur_node.left_child)
        if cur_node.right_child != None:
            self.__show_tree(cur_node.right_child)

tree = Tree()

for i in [23, 67, 12, 34, 55, 9]:
    tree.add(i)

print('Before reverse : ')
tree.show_tree()

reverse(tree)

print('After reverse : ')
tree.show_tree()
