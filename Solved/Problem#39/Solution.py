def find_k_subset(lst, k):
    return __find_k_subset(lst, [], k)

def __find_k_subset(lst, cur_itms, k):
    if sum(cur_itms) == k:
        return cur_itms
    if len(lst) == 0 or sum(cur_itms) > k:
        return None
    for i in range(len(lst)):
        x = __find_k_subset(lst[:i]+lst[i+1:], cur_itms+[lst[i]], k)
        if x != None:
            return x
