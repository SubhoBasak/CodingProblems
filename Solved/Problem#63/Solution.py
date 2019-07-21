# Solution part

def deepest_node(tree):
    if tree.root != None:
        height, deepest_node = __deepest_node(tree.root, 0)
        print(deepest_node.value)

def __deepest_node(cur_node, height):
    if cur_node.left_child == None and cur_node.right_child == None:
        return height, cur_node

    left_height = right_height = 0

    if cur_node.left_child != None:
        left_height, left_node = __deepest_node(cur_node.left_child, height+1)
    if cur_node.right_child != None:
        right_height, right_node = __deepest_node(cur_node.right_child, height+1)

    if left_height > right_height:
        return left_height, left_node
    return right_height, right_node

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

tree = Tree()
for i in range(5):
    tree.add(i)

deepest_node(tree)
