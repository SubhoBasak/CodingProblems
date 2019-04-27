class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(node):
    op_str = ''
    str_left = None
    str_right = None
    if node.left != None:
        str_left = serialize(node.left)
    if node.right != None:
        str_right = serialize(node.right)
    if str_left != None:
        op_str += ','+str_left
    if str_right != None:
        op_str += ','+str_right
    if op_str == '':
        return node.val
    else:
        return node.val+op_str

def deserialize(string):
    lst = string.split(',')
    tree = Node('root')
    for m, n in enumerate(lst[1:]):
        lst[m] = n.split('.')
    for i in lst[:len(lst)-1]:
        op_str = ''
        cur_node = tree
        for j in i:
            if j == 'left':
                if cur_node.left == None:
                    cur_node.left = Node(None)
                cur_node = cur_node.left
            if j == 'right':
                if cur_node.right == None:
                    cur_node.right = Node(None)
                cur_node = cur_node.right
        cur_node.val = '.'.join(i)
    return tree



tree = Node('root',
	Node('left', right = Node('left.right')),
	Node('right', Node('right.left', Node('right.left.left'), Node('right.left.right')), Node('right.right')))
x = serialize(tree)
Tree = deserialize(x)

def view(x, y):
    print(x.val, ':', y.val)
    if x.left != None and y.left != None:
        view(x.left, y.left)
    if x.right != None and y.right != None:
        view(x.right, y.right)

view(tree, Tree)
