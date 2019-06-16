lst = input().split(',')
lst = [int(i) for i in lst]

size = len(lst)
op_lst = []

for i in range(size):
    x = 1
    for j in range(1, size):
        m = i+j
        if m > size-1:
            m = m-size
        x *= lst[m]
    op_lst.append(x)

print(op_lst)
