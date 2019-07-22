def if_overlapped(lst):
    op_lst = [lst[0]]
    for i, j in lst[1:]:
        for x in range(len(op_lst)):
            m, n = op_lst[x]
            if i >= m and j <= n:
                continue
            elif m >= i and n <= j:
                op_lst[x] = (i, j)
                op_lst = if_overlapped(op_lst)
            elif i >= m and j >= n and i <= n:
                op_lst[x] = (m, j)
                op_lst = if_overlapped(op_lst)
            elif i <= m and j <= n and j >= m:
                op_lst[x] = (i, n)
                op_lst = if_overlapped(op_lst)
        op_lst.append((i, j))
    return op_lst
