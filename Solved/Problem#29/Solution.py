class node:
    def __init__(self, value = None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.lock = False

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
            print('value already in the tree !')

    def pre_order(self):
        self.__pre_order(self.root)

    def __pre_order(self, cur_node):
        print(cur_node.value)
        print(cur_node.lock)
        if cur_node.left_child != None:
            self.__pre_order(cur_node.left_child)
        if cur_node.right_child != None:
            self.__pre_order(cur_node.right_child)

    def find(self, value):
        return self.__find(self.root, value)

    def __find(self, cur_node, value):
        if cur_node.value == value:
            return cur_node
        elif value < cur_node.value:
            if cur_node.left_child != None:
                return self.__find(cur_node.left_child, value)
            print('Value is not in the tree !')
            return None
        elif value > cur_node.value:
            if cur_node.right_child != None:
                return self.__find(cur_node.right_child, value)
            print('Value is not in the tree !')
            return None

    def is_locked(self, value):
        return self.__ancestors(self.root, value)

    def __ancestors(self, cur_node, value):
        if cur_node.lock == True:
            return True
        elif cur_node.value == value:
            return self.__descendants(cur_node) # if all ancestors are unlocked
        elif value < cur_node.value:            # then it will check all the 
            if cur_node.left_child != None:     # descendants
                return self.__ancestors(cur_node.left_child, value)
            else:
                print('Value is not in the tree !')
                return None
        else:
            if cur_node.right_child != None:
                return self.__ancestors(cur_node.right_child, value)
            else:
                print('Value is not in the tree !')
                return None

    def __descendants(self, cur_node):
        if cur_node.lock == True:
            return True
        elif cur_node.left_child == None and cur_node.right_child == None:
            return False
        elif cur_node.left_child == None:
            return self.__descendants(cur_node.right_child)
        elif cur_node.right_child == None:
            return self.__descendants(cur_node.left_child)
        else:
            return self.__descendants(cur_node.left_child) or self.__descendants(cur_node.right_child)

    def lock(self, value):
        l = self.is_locked(value)
        if l == True:
            return False
        elif l == False:
            cur_node = self.find(value)
            cur_node.lock = True
            return True

    def unlock(self, value):
        cur_node = self.find(value)
        if cur_node.lock == True:
            cur_node.lock = False
            return True
        return False
