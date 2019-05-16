dct = input().split(',')
dct = list(map(lambda x: x.strip(), dct))
st = input()

# crate a priority queue for arranged the data
# after extracting it from the given string
class queue:
    def __init__(self):
        self.__items = []

    def enqueue(self, prity, value):
        self.__items.append([prity, value])

    def dequeue(self):
        mn_indx = 0
        for i in range(1, len(self.__items)):
            if self.__items[mn_indx][0] > self.__items[i][0]:
                mn_indx = i
        return self.__items.pop(mn_indx)

    def isEmpty(self):
        if len(self.__items) == 0:
            return True
        return False

q = queue()
op_lst = []

for i in dct:
    if i in st:
        indx = st.index(i)
        q.enqueue(indx, i)

while not q.isEmpty():
    op_lst.append(q.dequeue())

print(op_lst)
