# One (in constant space or O(1)) of the two (the other condition is in O(N)
# running time, which is not achived in this solution) conditions is satisfied
# in this solution

def mresure_volume(lst):
    mx = max(lst)
    volume = 0
    start = stop = None
    mid_part = 0
    for i in range(mx, 0, -1):
        for j in range(len(lst)):
            if i in lst:
                if lst[j] == i and start == None:
                    start = j
                elif lst[j] >= i and start != None:
                    mid_part += 1
                    stop = j
            else:
                if lst[j] > i and start == None:
                    start = j
                elif lst[j] >= i and start != None:
                    mid_part += 1
                    stop = j
        if start != None and stop != None:
            volume += stop - start - mid_part
        start = stop = None
        mid_part = 0
    return volume
