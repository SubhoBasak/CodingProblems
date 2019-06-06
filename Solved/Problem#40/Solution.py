class Stack:
    def __init__(self):
        self.__items = []

    def push(self, val):
        self.__items.append(val)

    def pop(self):
        return self.__items.pop()

    def max(self):
        return len(self.__items)
