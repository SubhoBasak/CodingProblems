# Solution part


def find_second(root):
     # fl = first largest ; sl = second largest
    fl, sl = __find_second(root, root.value, None)
    return sl

def __find_second(cur_node, fl, sl):
    if cur_node.value > fl:
        sl = fl
        fl = cur_node.value
    elif sl == None:
        sl = cur_node.value
    elif cur_node.value > sl:
        sl = cur_node.value

    l_fl = l_sl = None # l_fl = left first largest, l_sl = left second largest
    r_fl = r_sl = None # r_fl = right first largest, r_sl = right second largest

    if cur_node.left_node != None:
        l_fl, l_sl = __find_second(cur_node.left_node, fl, sl)
    if cur_node.right_node != None:
        r_fl, r_sl = __find_second(cur_node.right_node, fl, sl)
    lst = [fl, sl] # create a list to compare all the values, using max() and
                   # pop() function to find the curent second largest value
    if l_fl != None:
        lst += [l_fl, l_sl]
    if r_fl != None:
        lst += [r_fl, r_sl]
    indx = lst.index(max(lst)) # find the index of the current largest value in
                               # in the list
    fl = lst.pop(indx) # pop up the largest value from the list and assign it
                       # to the fl (first largest) variable
    sl = max(lst) # because we pop up the largest val form the list so it's the
                  # second largest val
    return fl, sl


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
