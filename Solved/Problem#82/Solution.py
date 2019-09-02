# Solution part

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

    def show_linked_list(self):
        if self.head != None:
            cur_node = self.head
            while cur_node != None:
                print(cur_node.value)
                cur_node = cur_node.nxt_node
        else:
            print('Linked list is empty !')

def decode_linked_list(lst):
    cur_node = lst.head
    m = 1
    digit = 0
    while cur_node != None:
        digit += m*cur_node.value
        m *= 10
        cur_node = cur_node.nxt_node
    return digit

def encode_linked_list(digit):
    digit = str(digit)
    lst = list(digit)
    lst.reverse()
    tmp_lnked_lst = linked_list()
    for i in lst:
        tmp_lnked_lst.add(i)
    return tmp_lnked_lst

def linked_list_element_sum(lst1, lst2):
    num1 = decode_linked_list(lst1)
    num2 = decode_linked_list(lst2)

    print('The tow numbers are :\n\t{num1} :: {num2}'.format(**{'num1': num1, 'num2': num2}))
    print('\nThe sum of these two numbers is : ', num1+num2)

    lst = encode_linked_list(num1+num2)

    print('After encode the numbers....')
    print('Linked list is :')
    lst.show_linked_list()
    
# Testing part

lst1 = linked_list()
for i in [1, 8, 4]:
    lst1.add(i)

lst2 = linked_list()
for i in [2, 0, 1]:
    lst2.add(i)

linked_list_element_sum(lst1, lst2)
