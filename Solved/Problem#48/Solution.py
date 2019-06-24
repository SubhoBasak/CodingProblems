def div_into_2(lst):
    total = sum(lst)
    sub_lst = find_item_sum_k(lst, [], total/2)
    if sub_lst == None:
        return None
    for i in sub_lst:
        lst.remove(i)
    return sub_lst, lst

def find_item_sum_k(lst, added, k):
    if len(lst) == 0:
        return None
    elif sum(added) == k:
        return added
    for i, j in enumerate(lst):
        sub_lst = find_item_sum_k(lst[:i]+lst[i+1:], added+[j], k)
        if sub_lst != None:
            return sub_lst
    return None
