class stack:
    def __init__(self):
        self.__items = []

    def push(self, value):
        self.__items.append(value)

    def pop(self):
        return self.__items.pop()

    def isEmpty(self):
        if len(self.__items) == 0:
            return True
        return False

    def getLast(self):
        return self.__items[len(self.__items)-1]

def is_matched(st):
    stk = stack()
    for i in st:
        if i == '(' or i == '{' or i == '[':
            stk.push(i)
        elif i == ')':
            if not stk.isEmpty() and stk.getLast() == '(':
                stk.pop()
            else:
                return False
        elif i == '}':
            if not stk.isEmpty() and stk.getLast() == '{':
                stk.pop()
            else:
                return False
        else:
            if i == ']' and not stk.isEmpty():
                stk.pop()
            else:
                return False
    return stk.isEmpty()

# after the all the operation above in the for loop is completed if the
# stack become empty thats mean no open bracets are left for close.
# so at the last the programme check that if the stack is empty, if it is
# then it will return True, and that True indicate that all bracets are
# matched so we return that True directly from the function insted of
# that :
#           if stk.isEmpty():
#               return True
#           return False
#
