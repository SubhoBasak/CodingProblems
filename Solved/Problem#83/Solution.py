# Solution part

def min_sum_of_path(tree):
    if tree.root == None:
        print("Tree is empty !")
        return None
    else:
        return __min_sum_of_path(tree.root)

def __min_sum_of_path(cur_node):
    left_path = right_path = None

    if cur_node.left_child != None:
        left_path = __min_sum_of_path(cur_node.left_child)
    if cur_node.right_child != None:
        right_path = __min_sum_of_path(cur_node.right_child)

    if left_path == None and right_path == None:
        return cur_node.value
    elif right_path == None:
        return cur_node.value+left_path
    elif left_path == None:
        return cur_node.value+right_path
    else:
        return cur_node.value+min(left_path, right_path)

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
        else:
            print("Value already in tree !")


tree = Tree()
for i in [43, 78, 55, 10, 21, 56, 78]:
    tree.add(i)
print(min_sum_of_path(tree))
