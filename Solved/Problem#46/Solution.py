# Solution part

def evaluate_bin_tree_exp(root):
    if root.value in ['+', '-', '*', '/']:
        left_val = evaluate_bin_tree_exp(root.left_child)
        right_val = evaluate_bin_tree_exp(root.right_child)
        return eval(str(left_val)+root.value+str(right_value))
    else:
        return root.value

# Testing part will be soon...
