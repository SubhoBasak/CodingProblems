def make_tree_pre_in(pre_ord, in_ord):
    p_queue = priority_queue()
    __make_tree_pre_in(pre_ord, in_ord, 0, p_queue)
    tree = Tree()
    while not p_queue.isEmpty():
        x = p_queue.dequeue()
        tree.add(x)
    return tree

def __make_tree_pre_in(pre_ord, in_ord, level, Q):
    root = pre_ord.pop(0)
    indx = in_ord.index(root)
    left_in = in_ord[:indx]
    right_in = []
    if indx+1 < len(in_ord):
        right_in = in_ord[indx+1:]
    Q.enqueue([level, root])
    in_ord.pop(indx)
    indx = len(left_in)
    if len(left_in) != 0:
        left_pre = pre_ord[:indx]
        __make_tree_pre_in(left_pre, left_in, level+1, Q)
    if len(right_in) != 0:
        right_pre = pre_ord[indx:]
        __make_tree_pre_in(right_pre, right_in, level+1, Q)

class priority_queue:
    def __init__(self):
        self.__items = []

    def enqueue(self, value):
        self.__items.append(value)

    def dequeue(self):
        mn = 0
        for i in range(1, len(self.__items)):
            if self.__items[i][0] < self.__items[mn][0]:
                mn = i
        return self.__items.pop(mn)[1]

    def isEmpty(self):
        if len(self.__items) == 0:
            return True
        return False

class node:
    def __init__(self, value = None):
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
        if value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = node(value)
            else:
                self.__add(cur_node.right_child, value)

    def pre_order(self):
        if self.root != None:
            self.__pre_order(self.root)

    def __pre_order(self, cur_node):
        print(cur_node.value)
        if cur_node.left_child != None:
            self.__pre_order(cur_node.left_child)
        if cur_node.right_child != None:
            self.__pre_order(cur_node.right_child)

    def in_order(self):
        if self.root != None:
            self.__in_order(self.root)

    def __in_order(self, cur_node):
        if cur_node.left_child != None:
            self.__in_order(cur_node.left_child)
        print(cur_node.value)
        if cur_node.right_child != None:
            self.__in_order(cur_node.right_child)
