# Solution part

def reverse(lst):
    prv = None
    cur = lst.head
    nxt = cur.nxt_node
    while nxt != None:
        cur.nxt_node = prv
        prv = cur
        cur = nxt
        nxt = cur.nxt_node
    cur.nxt_node = prv
    lst.head = cur

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

    def show_lst(self):
        cur_node = self.head
        while cur_node != None:
            print(cur_node.value, end = ', ')
            cur_node = cur_node.nxt_node
        print()

lst = linked_list()
for i in range(500):
    lst.add(i)

lst.show_lst()

reverse(lst)

lst.show_lst()
