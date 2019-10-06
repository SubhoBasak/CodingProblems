# Solution part

def swap_two_linked_list_items(head):
    if head.nxt_node != None:
        nxt_node = head.nxt_node
        n_val = nxt_node.value
        nxt_node.value = head.value
        head.value = n_val
        if nxt_node.nxt_node != None:
            swap_two_linked_list_items(nxt_node.nxt_node)

# Testing part

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

    def show_list(self):
        cur_node = self.head
        while cur_node != None:
            print(cur_node.value, end = '->')
            cur_node = cur_node.nxt_node
        print()

lnk_lst = linked_list()
for i in range(5):
    lnk_lst.add(i)

print('Before swap :')
lnk_lst.show_list()

swap_two_linked_list_items(lnk_lst.head)

print('After swap :')
lnk_lst.show_list()
