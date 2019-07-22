def can_modified(lst):
    x = 0
    for i in range(len(lst)-1):
        if lst[i] <= lst[i+1]:
            continue
        x += 1
        if x > 1:
            return False
    return True
