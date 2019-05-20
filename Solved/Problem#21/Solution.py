# Solution part

def remove(lst, k):
    indx = len(lst) - k # calculate the last k th element index
    cur_node = lst.head
    cur_indx = 0
    if k == 0:
        lst.head = lst.head.nxt_node
    while cur_indx+1 != indx:
        cur_node = cur_node.nxt_node
        cur_indx += 1
    cur_node.nxt_node = cur_node.nxt_node.nxt_node



# Testing part

class node:
    def __init__(self, value = None):
        self.value = value
        self.nxt_node = None

class linked_list:
    def __init__(self):
        self.head = None

    def add(self, value):
        if self.head == None:
            self.head = node(value)
        else:
            cur_node = self.head
            while cur_node.nxt_node != None:
                cur_node = cur_node.nxt_node
            cur_node.nxt_node = node(value)

    def view(self):
        cur_node = self.head
        while cur_node != None:
            print(cur_node.value, end = ', ')
            cur_node = cur_node.nxt_node

    def __len__(self):
        cur_size = 0
        cur_node = self.head
        while cur_node != None:
            cur_size += 1
            cur_node = cur_node.nxt_node
        return cur_size

lnk_lst = linked_list()
for i in range(10):
    lnk_lst.add(i)
print('before remove')
lnk_lst.view()
remove(lnk_lst, 7)
print('\nafter remove')
lnk_lst.view()
