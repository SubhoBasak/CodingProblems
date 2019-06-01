# Tree class
class Tree:
# Create a list of None values of size of the maximum possible number of nodes
# fot the given height could be, to store the tree node's value

# we know that max_node = 2^(height+1)-1
    def __init__(self, height):
        self.__items = [None for i in range(2**(height+1)-1)]

# Add a new data element to the tree in the proper position. But this function
# does not do any job, it just call it's helper method with right patameters
    def add(self, value):
        return self.__add(0, value)+1

# Helper method for the previous method
    def __add(self, cur_indx, value):
        if self.__items[cur_indx] == None:
            self.__items[cur_indx] = value
            return cur_indx
        elif self.__items[cur_indx] > value:
            return self.__add(2*cur_indx+1, value)
        elif self.__items[cur_indx] < value:
            return self.__add(2*cur_indx+2, value)

# Find and return the node conatin the given value if it exist in the tree,
# otherwise return none
    def find(self, value):
        return self.__find(0, value)

    def __find(self, cur_indx, value):
        if self.__items[cur_indx] == value:
            return cur_indx
        elif value < self.__items[cur_indx] and 2*cur_indx+1 < len(self.__items):
            return self.__find(2*cur_indx+1, value)
        elif value > self.__items[cur_indx] and 2*cur_indx+2 < len(self.__items):
            return self.__find(2*cur_indx+2, value)
        else:
            print('Value is not in available in the tree !')
            return None

# Delete the node contain the value matched with the given value if it exist in
# the tree and sort the tree to maintain it's property and return the index form
# where it remove the value. And again as the Previous add method it does
# nothing, it just call it's helper method with proper parameter
    def delete(self, value):
        indx = self.find(value)
        if indx == None:
            return None
        return self.__delete(indx)+1

# Helper method for the previous method fot search the given value in the tree
# and delete it and then calls it's helper method to sort the tree
    def __delete(self, cur_indx):
        if (2*cur_indx+1 >= len(self.__items) or self.__items[2*cur_indx+1] == None) and (2*cur_indx+2 >= len(self.__items) or self.__items[2*cur_indx+2] == None):
            self.__items[cur_indx] = None
            return cur_indx
        elif 2*cur_indx+2 < len(self.__items) or self.__items[2*cur_indx+2] == None:
            indx = self.__max_node(2*cur_indx+2)
            self.__items[cur_indx] = self.__items[indx]
            self.__delete(indx)
            return cur_indx
        else:
            indx = self.__min_node(2*cur_indx+1)
            self.__items[cur_indx] = self.__items[indx]
            self.__delete(indx)
            return cur_indx

    def __min_node(self, cur_indx):
        while 2*cur_indx+1 < len(self.__items) and self.__items[2*cur_indx+1] != None:
            cur_indx = 2*cur_indx+1
        return cur_indx

    def __max_node(self, cur_indx):
        while 2*cur_indx+2 < len(self.__items) and self.__items[2*cur_indx+2] != None:
            cur_indx = 2*cur_indx+2
        return cur_indx

def main():
    op = []
    k = int(input())
    tree = Tree(k)
    for i in range(k):
        inp = input().split(' ')
        if inp[0] == 'i':
            op.append(tree.add(int(inp[1])))
        elif inp[0] == 'd':
            op.append(tree.delete(int(inp[1])))
        else:
            print('Invalid command')
        print(tree._Tree__items[:8])
    for i in op:
        print(i)

if __name__ == '__main__':
    main()
