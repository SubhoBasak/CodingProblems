#Main solution part

def find_intersection(lst1, lst2):
    if lst1.head == None:
        len1 = 0
    else:
        cur_node = lst1.head
        len1 = 1
        while cur_node.nxt_node != None:
            cur_node = cur_node.nxt_node
            len1 += 1
    if lst2.head == None:
        len2 = 0
    else:
        cur_node = lst2.head
        len2 = 1
        while cur_node.nxt_node != None:
            cur_node = cur_node.nxt_node
            len2 += 1
    if len1 > len2:
        cur_node1 = lst1.head
        cur_node2 = lst2.head
        for i in range(len1-len2):
            cur_node1 = cur_node1.nxt_node
    if len1 < len2:
        cur_node1 = lst1.head
        cur_node2 = lst2.head
        for i in range(lst2-lst1):
            cur_node2 = cur_node2.nxt_node
    for i in range(min(len1, len2)):
        if cur_node1.value == cur_node2.value:
            print(cur_node1.value)
            break
        cur_node1 = cur_node1.nxt_node
        cur_node2 = cur_node2.nxt_node


#Testing part

class node:
    def __init__(self, value):
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



lst1 = linked_list()
lst2 = linked_list()
for i in range(9):
    lst1.add(i)

	
for i in ['a', 'b', 'c', 'd', 'e']:
    lst2.add(i)

	
lst2.head.nxt_node.nxt_node.nxt_node.nxt_node.nxt_node = lst1.head.nxt_node.nxt_node.nxt_node.nxt_node.nxt_node.nxt_node.nxt_node
find_intersection(lst1, lst2)
