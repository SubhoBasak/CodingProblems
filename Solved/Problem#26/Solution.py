def edit_distance(str1, str2):
    str1 = list(str1)
    str2 = list(str2)
    i, j = 0, 0
    dis = 0
    while i < len(str1) and j < len(str2):
        if str1[i] != str2[j]:
            dis += 1
        i += 1
        j += 1
    if i == len(str1):
        dis += len(str2)-len(str1)
    elif j == len(str2):
        dis += len(str1)-len(str2)
    return dis
