def return_first_recurring_charecter(st):
    prv = st[0]
    for i in st[1:]:
        if i == prv:
            return i
        prv = i
    return None
