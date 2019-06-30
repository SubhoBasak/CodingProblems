def clockwise_spiral(mat):
    op_lst = []
    while len(mat) != 0 and len(mat[0]) > 0:
        if len(mat) > 0 and len(mat[0]) > 0:
            for i in mat[0]:
                op_lst.append(i)
            mat.pop(0)

        if len(mat) > 0 and len(mat[0]) > 0:
            for i in mat:
                op_lst.append(i.pop())

        if len(mat) > 0 and len(mat[0]) > 0:
            for i in mat[len(mat)-1][::-1]:
                op_lst.append(i)
            mat.pop()

        if len(mat) > 0 and len(mat[0]) > 0:
            for i in mat[::-1]:
                op_lst.append(i.pop(0))

    return op_lst
