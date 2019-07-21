class Stack:
    def __init__(self):
        self.__items = []
        self.max_value = None

    def push(self, value):
        self.__items.append(value)
        if self.max_value == None:
            self.max_value = value
        elif value > self.max_value:
            self.max_value = value

    def pop(self):
        if len(self.__items) == 0:
            return None
        else:
            x =  self.__items.pop()
            if x == self.max_value:
                if len(self.__items) != 0:
                    self.max_value = max(self.__items)
                else:
                    self.max_value = None
            return x

    def max(self):
        return self.max_value
