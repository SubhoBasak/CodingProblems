def length(lst):
    if len(lst) != 0:
        lnt = 0
        for i in lst:
            lnt += len(i)
        return len(lst)-1+lnt
    return 0

def align_text(txt, k):
    lst = txt.split(' ')
    op_lst = [[]]
    cur_indx = 0
    for i in lst:
        ln = length(op_lst[cur_indx])
        if ln == 0:
            op_lst[cur_indx].append(i)
        elif len(i)+1+ln <= k:
            op_lst[cur_indx].append(i)
        else:
            op_lst.append([])
            cur_indx += 1
            op_lst[cur_indx].append(i)
    return op_lst
