class iterator:
    def __init__(self, arr):
        self.arr = arr
        if len(self.arr) != 0:
            self.cur_item = self.arr.pop(0)

    def next(self):
        if len(self.cur_item) != 0:
            return self.cur_item.pop(0)
        elif len(self.arr) != 0:
            self.cur_item = self.arr.pop(0)
            return self.next()
        else:
            raise ValueError

    def has_next(self):
        if len(self.cur_item) != 0:
            return True
        elif len(self.arr) != 0:
            for i in self.arr:
                if len(i) != 0:
                    return True
        return False
