class zero_array_structure:
    def __init__(self, arr, size):
        self.size = size
        self.arr = []

        tmp = 0
        for i in arr:
            if i != 0:
                if tmp != 0:
                    self.arr.append([tmp])
                    tmp = 0
                self.arr.append(i)
            else:
                tmp += 1
        if tmp != 0:
            self.arr.append([tmp])
            tmp = 0

    def set(self, i, val):
        if i < self.size and i >= 0:
            cur = -1
            indx = 0
            while cur != i:
                if type(self.arr[indx]) == int:
                    cur += 1
                    if cur == i:
                        break
                    indx += 1
                elif type(self.arr[indx]) == list:
                    tmp = cur
                    cur += self.arr[indx][0]
                    if cur >= i:
                        left = i-tmp-1
                        right = cur-i
                        tmp_indx = indx
                        self.arr.pop(indx)
                        if left > 0:
                            self.arr.insert(tmp_indx, [left])
                            tmp_indx += 1
                        self.arr.insert(tmp_indx, 0)
                        indx = tmp_indx
                        tmp_indx += 1
                        if right > 0:
                            self.arr.insert(tmp_indx, [right])
                        break
                    elif cur < i:
                        indx += 1
            self.arr[indx] = val
        else:
            print('Invalid index !')
        if val == 0:
            arr = self.arr
            self.arr = []
            tmp = 0
            for i in arr:
                if type(i) == list:
                    tmp += i[0]
                elif i == 0:
                    tmp += 1
                else:
                    if tmp != 0:
                        self.arr.append([tmp])
                        tmp = 0
                    self.arr.append(i)
            if tmp != 0:
                self.arr.append([tmp])

    def get(self, i):
        if i < self.size and i >= 0:
            cur = -1
            for j in self.arr:
                if type(j) == int:
                    cur += 1
                    if cur == i:
                        return j
                elif type(j) == list:
                    if cur+j[0] >= i:
                        return 0
                    elif cur+j[0] < i:
                        cur = cur+j[0]
        else:
            print('Invalid index !')
