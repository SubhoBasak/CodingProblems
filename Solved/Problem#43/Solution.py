def max_profit(lst):
    best_buy = None
    best_sell = None

    i = lst[0]
    j = None

    for k in lst[1:]:
        if k < i:
            i = k
        elif k > i:
            if j == None:
                j = k
            elif k > j:
                j = k
        if j != None:
            if best_buy == None:
                best_buy = i
                best_sell = j
            elif best_sell-best_buy < j-i:
                best_buy = i
                best_sell = j

    return best_buy
