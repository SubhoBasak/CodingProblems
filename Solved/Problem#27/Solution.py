def running_median(seq):
    tmp = []
    op = []
    for i in seq:
        tmp.append(i)
        tmp.sort()
        if len(tmp)%2 == 1:
            op.append(tmp[int(len(tmp)/2)])
        else:
            a = tmp[int(len(tmp)/2)-1]
            b = tmp[int(len(tmp)/2)]
            op.append((a+b)/2)
        return op
