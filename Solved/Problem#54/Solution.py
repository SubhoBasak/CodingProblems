# Solution part

def deepest_node(root):
    return __deepest_node(root, 0)[0]

def __deepest_node(root, height):
    if root.left_child == None and root.right_child == None:
        return root, height

    left_node = right_node = (root, height)
    if root.left_child != None:
        left_node = __deepest_node(root.left_child, height+1)
    if root.right_child != None:
        right_node = __deepest_node(root.right_child, height+1)

    if left_node[1] >= right_node[1]:
        return left_node
    else:
        return right_node


# Testing part

class node:
    def __init__(self, value = None):
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

    def show_tree(self):
        self.__show_tree(self.root)

    def __show_tree(self, cur_node):
        if cur_node != None:
            print(cur_node.value)
            self.__show_tree(cur_node.left_child)
            self.__show_tree(cur_node.right_child)

Tree = tree()

for i in [23, 44, 45, 35, 56, 67]:
    Tree.add(i)

Tree.show_tree()

print('\nDeepest node : ', deepest_node(Tree.root).value)
