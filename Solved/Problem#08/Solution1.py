# copied from cs dojo
# not efficient method

def is_unv(root):
    if root == None:
        return True
    if root.left != None and root.left.value != root.value:
        return False
    if root.right != None and root.right.value != root.value:
        return False
    if is_unv(root.left) and is_unv(root.right):
        return True
    return False

def cunt_unv(root):
    if root == None:
        return 0
    total = cunt_unv(root.left) + cunt_unv(root.right)
    if is_unv(root):
        total += 1
    return total
