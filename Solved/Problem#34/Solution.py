#Using library function
import itertools as it

def subsets1(lst):
    tmp = []
    for i in range(len(lst)+1):
        tmp.append(list(it.combinations(lst, i)))
    return tmp

#Without using library function
def combinations(lst, n):
    if n == 0:
        return [[]]
    tmp = []
    for i in range(len(lst)):
        comb = combinations(lst[i+1:], n-1)
        for j in comb:
            j.insert(0, lst[i])
        tmp += comb
    return tmp

def subsets2(lst):
    tmp = []
    for i in range(len(lst)+1):
        tmp += combinations(lst, i)
    return tmp
