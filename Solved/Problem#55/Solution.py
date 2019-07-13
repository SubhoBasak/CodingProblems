# Solution part

def merge_linked_list(*lst):
    op_lst = []
    indx_lst = []
    for i in lst:
        indx_lst.append(i.head)

    while len(indx_lst) != 0:
        tmp_indx = 0
        mn = indx_lst[0].value
        for i in range(1, len(indx_lst)):
            if indx_lst[i].value < mn:
                mn = indx_lst[i].value
                tmp_indx = i
        op_lst.append(mn)
        if indx_lst[tmp_indx].nxt_node != None:
            indx_lst[tmp_indx] = indx_lst[tmp_indx].nxt_node
        else:
            indx_lst.pop(tmp_indx)
    return op_lst

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
            
lst1 = linked_list()
lst2 = linked_list()
lst3 = linked_list()
lst4 = linked_list()

for i in [1, 2, 4, 6, 8]:
    lst1.add(i)

for i in [2, 2, 4, 6]:
    lst2.add(i)

for i in [0, 1, 5]:
    lst3.add(i)

for i in [3, 4, 8, 9]:
    lst4.add(i)

print(merge_linked_list(lst1, lst2, lst3, lst4))
