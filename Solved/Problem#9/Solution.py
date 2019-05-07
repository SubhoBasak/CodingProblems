lst = input()
lst = lst.split(',')
lst = [int(i) for i in lst]

incl = lst[0]
excl = 0

for i in lst[1:]:
    tmp = incl
    incl = max(excl+i, incl)
    excl = tmp

print(incl)
