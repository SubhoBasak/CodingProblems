def find_itinerary(lst):
    return __find_itinerary(lst, None)

def __find_itinerary(lst1, lst2):
    if lst2 != None:
# this for loop must be keep first to get the output, lexicographically smaller
        for i in range(len(lst1)):
            if lst1[i][0] == lst2[len(lst2)-1]:
                tmp = lst1.pop(i)
                lst2.append(tmp[1])
                if len(lst1) != 0:
                    return __find_itinerary(lst1, lst2)
                return lst2
# this for loop must be keep first to get the output, lexicographically bigger
        for i in range(len(lst1)):
            if lst1[i][1] == lst2[0]:
                tmp = lst1.pop(i)
                tmp += lst2[1:]
                if len(lst1) != 0:
                    return __find_itinerary(lst1, tmp)
                return tmp
    for i in range(len(lst1)):
        for j in range(i, len(lst1)):
            if i != j and lst1[i][1] == lst1[j][0]:
                tmp2 = lst1.pop(j)#here j in poped up first because if we poped
                tmp1 = lst1.pop(i)#up i first then current jth element's index
                tmp1.append(tmp2[1])#would be changed. because i in less than j
                if len(lst1) != 0:
                    return __find_itinerary(lst1, tmp1)
                return tmp2
