def plaindrome(st):
    if st[0] == st[len(st)-1]:
        if len(st) == 2:
            return st
        return st[0]+plaindrome(st[1:len(st)-1])+st[0]
    elif len(st) == 2:
        if st[0] < st[1]:
            return st+st[0]
        return st[1]+st
    else:
        st1 = st[len(st)-1]+plaindrome(st[0:len(st)-1])+st[len(st)-1]
        st2 = st[0]+plaindrome(st[1:len(st)])+st[0]
        if len(st1) < len(st2):
            return st1
        elif len(st1) > len(st2):
            return st2
        else:
            return min(st1, st2)
