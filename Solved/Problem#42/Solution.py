def plaindromic_string(st):
    if len(st) == 1:
        return st
    elif st[0] ==  st[len(st)-1]:
        if len(st) == 2:
            return st
        sub_st = plaindromic_string(st[1:len(st)-1])
        if sub_st != None:
            return st[0]+sub_st+st[0]
        return None
    elif len(st) == 2:
        return None
    else:
        st1 = plaindromic_string(st[0:len(st)-1])
        st2 = plaindromic_string(st[1:len(st)])
        if st1 == None:
            return st2
        elif st2 == None:
            return st1
        elif len(st1) < len(st2):
            return st2
        elif len(st1) > len(st2):
            return st1
        else:
            return min(st1, st2)
