def count_invertion(lst):
    x = 0
    for i, j in enumerate(lst):
        for k in lst[i+1:]:
            if k < j:
                x += 1

    return x
