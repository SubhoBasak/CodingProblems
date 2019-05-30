# Solution part


def find_second(root):
    cur_node = root
    prv_node = None
    while cur_node.right_node != None:
        prv_node = cur_node
        cur_node = cur_node.right_node
    if cur_node.left_node != None:
        return cur_node.left_node.value
    return prv_node.value

# Testing part


class node:
    def __init__(self, value = None):
        self.value = value
        self.left_node = None
        self.right_node = None

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
            if cur_node.left_node == None:
                cur_node.left_node = node(value)
            else:
                self.__add(cur_node.left_node, value)
        elif value > cur_node.value:
            if cur_node.right_node == None:
                cur_node.right_node = node(value)
            else:
                self.__add(cur_node.right_node, value)

tree = Tree()
arr = [23, 12, 31, 4, 15, 29, 35, 2, 7, 25, 30, 33]

for i in arr:
    tree.add(i)

print('Second largest number is : ', find_second(tree.root))
