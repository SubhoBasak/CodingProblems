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
class queue:
    def __init__(self):
        self.stack1 = stack()
        self.stack2 = stack()

    def enqueue(self, value):
        self.stack1.push(value)

    def dequeue(self):
        while not self.stack1.isEmpty():
            self.stack2.push(self.stack1.pop())
        tmp = self.stack2.pop()
        while not self.stack2.isEmpty():
            self.stack1.push(self.stack2.pop())
        return tmp
