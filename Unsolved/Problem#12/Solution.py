# Tree class
class Tree:
# Create a list of None values of the given size to store the tree node's value
    def __init__(self, size):
        self.__items = [None for i in range(size)]

# Add a new data element to the tree in the proper position. But this function
# does not do any job, it just call it's helper method with right patameters
    def add(self, value):
        self.__add(0, value)

# Helper method for the previous method
    def __add(self, cur_indx, value):
        if self.__items[cur_indx] == None:
            self.__items[cur_indx] = value
            return cur_indx
        elif self.__items[cur_indx] > value:
            self.__add(2*cur_indx+1, value)
        elif self.__items[cur_indx] < value:
            self.__add(2*cur_indx+2, value)

# Delete the node contain the value matched with the given value if it exist in
# the tree and sort the tree to maintain it's property and return the index form
# where it remove the value. And again as the Previous add method it does
# nothing, it just call it's helper method with proper parameter
    def delete(self, value):
        self.__delete(0, value)

# Helper method for the previous method fot search the given value in the tree
# and delete it and then calls it's helper method to sort the tree
    def __delete(self, cur_indx, value):
        if self.__items[cur_indx] == value:
            if 2*cur_indx+1 < len(self.__items) or self.__items[2*cur_indx+1] == None:
                if 2*cur_indx+2 < len(self.__items) or self.__items[2*cur_indx+2] == None:
                    self.__items[cur_indx] = None
# If which node it will delete, has no chile node then its not resquired to sort
            else:
                self.__items[cur_indx] = None
                self.__sort(cur_indx)
            return cur_indx

# If the given value is not exist in the current index then it will check if the
# given value is less than the current node's value or greater than.
        elif self.__items[cur_node] > value:
# If it's less than, then the function check if the left child node is exist or
# not. If it exist then the funcion call itself with the left child's index,
# otherwise return None
            if 2*cur_indx+1 < len(self.__items):
                self.__delete(2*cur_indx+1, value)
            else:
                return None
        elif self.__items[cur_indx] < value:
# If it's greater than, then the function check if the right chile node if exist
# or not. If it exist then the function call itself with the right child's index
# otherwise return None
            if 2*cur_indx+2 < len(self.__items):
                self.__delete(2*cur_indx+2, value)
            else:
                return None

    def __sort(self, cur_indx):
        pass
