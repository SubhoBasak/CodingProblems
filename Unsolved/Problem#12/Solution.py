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

# Delete the node contain the value matched with the given value if it exist in
# the tree and sort the tree to maintain it's property and return the index form
# where it remove the value. And again as the Previous add method it does
# nothing, it just call it's helper method with proper parameter
    def delete(self, value):
        return self.__delete(0, value)+1

# Helper method for the previous method fot search the given value in the tree
# and delete it and then calls it's helper method to sort the tree
    def __delete(self, cur_indx, value):
        if self.__items[cur_indx] == value:
            self.__items[cur_indx] = None
            self.__sort(cur_indx)
            return cur_indx
# If the given value is not exist in the current index then it will check if the
# given value is less than the current node's value or greater than.
        elif self.__items[cur_indx] > value:
# If it's less than, then the function check if the left child node is exist or
# not. If it exist then the funcion call itself with the left child's index,
# otherwise return None
            if 2*cur_indx+1 < len(self.__items):
                return self.__delete(2*cur_indx+1, value)
            else:
                return None
        elif self.__items[cur_indx] < value:
# If it's greater than, then the function check if the right chile node if exist
# or not. If it exist then the function call itself with the right child's index
# otherwise return None
            if 2*cur_indx+2 < len(self.__items):
                return self.__delete(2*cur_indx+2, value)
            else:
                return None

# Helper method for the previous method to sort the tree.
    def __sort(self, cur_indx):
        left = right = None
# If the left child's index in range of the array then the left child is assign
# to the left variable
        if 2*cur_indx+1 < len(self.__items):
            left = self.__items[2*cur_indx+1]
# If the right child's index in range of the array then the right child is
# assign to the right variable
        if 2*cur_indx+2 < len(self.__items):
            right = self.__items[2*cur_indx+2]
# Check if the left and right both child exist then compare the child's value
# which child's value is greater, is assign to the current node and assign it
# none value and for it's sub-tree the sort function is call again
        if left != None and right != None:
            mx_indx = self.__items.index(max(self.__items[2*cur_indx+1], self.__items[2*cur_indx+2]))
            self.__items[cur_indx] = self.__items[mx_indx]
            self.__items[mx_indx] = None
            self.__sort(mx_indx)
        elif left == None and right != None:
            self.__items[cur_indx] = self.__items[2*cur_indx+2]
            self.__items[2*cur_indx+2] = None
            self.__sort(2*cur_indx+2)
        elif right == None and left != None:
            self.__items[cur_indx] = self.__items[2*cur_indx+1]
            self.__items[2*cur_indx+1] = None
            self.__sort(2*cur_indx+1)

def main():
    op = []
    k = int(input())
    tree = Tree(k)
    for i in range(k):
        inp = input().split(' ')
        if inp[0] == 'i':
            op.append(tree.add(int(inp[1])))
        elif inp[0] == 'd':
            op.append(tree.add(int(inp[1])))
        else:
            print('Invalid command')
    for i in op:
        print(i)

#if __name__ == '__main__':
#    main()
