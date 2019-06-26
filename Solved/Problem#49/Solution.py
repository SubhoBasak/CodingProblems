def find_word(mat, wrd):
    for i in mat:
        x = word_matcher(i, wrd)
        if x == True:
            return True
    for i in range(len(mat[0])):
        tmp_lst = []
        for j in range(len(mat)):
            tmp_lst.append(mat[j][i])
        x = word_matcher(tmp_lst, wrd)
        if x == True:
            return True
    return False

def word_matcher(lst, wrd):
    if len(lst) == 1:
        return False
    tmp = ''
    for i in lst:
        tmp += i
    if tmp == wrd:
        return True
    x = word_matcher(lst[:len(lst)-1], wrd)
    if x == True:
        return True
    x = word_matcher(lst[1:], wrd)
    if x == True:
        return True
    return False
